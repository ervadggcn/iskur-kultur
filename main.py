from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field, field_validator
from typing import List
import re

# Yazdığımız diğer dosyaları içeri aktarıyoruz
import models
from database import engine, SessionLocal

# Veritabanı tablolarını otomatik oluştur (yoksa yaratır)
models.Base.metadata.create_all(bind=engine)

# FastAPI uygulamamızı başlatıyoruz
app = FastAPI(
    title="BUÜ Kültür Merkezi API",
    description="Kültür Merkezi Randevu Yönetim Sistemi Backend'i"
)

# CORS Ayarları: Frontend (HTML/JS) farklı bir porttan çalışırken
# API'ye istek atabilsin diye izin veriyoruz.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Geliştirme aşamasında her yere açık
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------
# ARAYÜZ (FRONTEND) SUNUCU AYARLARI
# ---------------------------------------------------------

# 1. CSS ve resim dosyaları için assets klasörünü dışa açıyoruz
app.mount("/assets", StaticFiles(directory="assets"), name="assets")


# 2. Ana adrese (http://127.0.0.1:8000/) girildiğinde index.html'i göster
@app.get("/")
def serve_frontend():
    return FileResponse("index.html")


# Her istekte veritabanı bağlantısı açıp kapatan yardımcı fonksiyon
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------------------------------------
# 1. PYDANTIC ŞEMALARI (Veri Doğrulama / İş Kuralları)
# ---------------------------------------------------------

class RandevuBase(BaseModel):
    bina_adi: str
    oda_adi: str
    basvuru_tipi: str = Field(..., description="Sadece 'Kişi' veya 'Kurum' olabilir")
    topluluk_kisi_adi: str
    tarih: str
    saat_baslangic: str
    saat_bitis: str
    talep_not: str | None = None  # Opsiyonel alan

    # KURAL 1: Başvuru Tipi Kontrolü
    @field_validator('basvuru_tipi')
    def validate_basvuru_tipi(cls, value):
        if value not in ["Kişi", "Kurum"]:
            raise ValueError("Başvuru tipi sadece 'Kişi' veya 'Kurum' olabilir.")
        return value

    # KURAL 2: Tam Saat ve Mesai Kontrolü (08:00 - 22:00)
    @field_validator('saat_baslangic', 'saat_bitis')
    def validate_saat(cls, value):
        # Sadece 08:00 ile 22:00 arasındaki TAM SAATLERİ kabul eden Regex
        if not re.match(r"^(0[8-9]|1[0-9]|2[0-2]):00$", value):
            raise ValueError("Saatler 08:00 - 22:00 arasında ve tam saat (Örn: 13:00) formatında olmalıdır.")
        return value


class RandevuCreate(RandevuBase):
    pass


class RandevuResponse(RandevuBase):
    id: int

    # SQLAlchemy modelinden Pydantic modeline dönüşüme izin ver
    class Config:
        from_attributes = True


# ---------------------------------------------------------
# 2. API UÇ NOKTALARI (ENDPOINTS)
# ---------------------------------------------------------

@app.post("/api/randevu", response_model=RandevuResponse)
def create_randevu(randevu: RandevuCreate, db: Session = Depends(get_db)):
    # 1. Mantıksal Zaman Kontrolü
    if randevu.saat_bitis <= randevu.saat_baslangic:
        raise HTTPException(status_code=400, detail="Bitiş saati, başlangıç saatinden ileride olmalıdır.")

    # 2. Çakışma Kontrolü
    cakisan_randevu = db.query(models.Randevu).filter(
        models.Randevu.bina_adi == randevu.bina_adi,
        models.Randevu.oda_adi == randevu.oda_adi,
        models.Randevu.tarih == randevu.tarih,
        models.Randevu.saat_baslangic < randevu.saat_bitis,
        models.Randevu.saat_bitis > randevu.saat_baslangic
    ).first()

    if cakisan_randevu:
        raise HTTPException(status_code=400, detail="Seçilen tarih ve saat aralığında bu salon doludur.")

    # 3. Kayıt İşlemi
    yeni_randevu = models.Randevu(**randevu.model_dump())
    db.add(yeni_randevu)
    db.commit()
    db.refresh(yeni_randevu)

    return yeni_randevu


@app.get("/api/randevular/{bina_adi}", response_model=List[RandevuResponse])
def get_randevular(bina_adi: str, db: Session = Depends(get_db)):
    # İlgili binaya ait TÜM randevuları getirir. (Renk/Geçmiş ayrımını Frontend yapacak)
    randevular = db.query(models.Randevu).filter(models.Randevu.bina_adi == bina_adi).all()
    return randevular


@app.delete("/api/randevu/{randevu_id}")
def delete_randevu(randevu_id: int, db: Session = Depends(get_db)):
    randevu = db.query(models.Randevu).filter(models.Randevu.id == randevu_id).first()
    if not randevu:
        raise HTTPException(status_code=404, detail="Randevu bulunamadı.")
    db.delete(randevu)
    db.commit()
    return {"message": "Randevu başarıyla silindi."}


@app.put("/api/randevu/{randevu_id}")
def update_randevu(randevu_id: int, randevu: RandevuCreate, db: Session = Depends(get_db)):
    db_randevu = db.query(models.Randevu).filter(models.Randevu.id == randevu_id).first()
    if not db_randevu:
        raise HTTPException(status_code=404, detail="Randevu bulunamadı.")

    # Güncelleme işlemi
    for key, value in randevu.model_dump().items():
        setattr(db_randevu, key, value)

    db.commit()
    db.refresh(db_randevu)
    return db_randevu