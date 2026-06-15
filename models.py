from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base


class Randevu(Base):
    __tablename__ = "randevular"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    bina_adi = Column(String, index=True, nullable=False)
    oda_adi = Column(String, index=True, nullable=False)

    # Özellikler
    basvuru_tipi = Column(String, nullable=False)  # "Kişi" veya "Kurum"
    topluluk_kisi_adi = Column(String, nullable=False)

    # Tarih ve saatleri metin (TEXT) olarak tutuyoruz
    tarih = Column(String, index=True, nullable=False)  # Örn: "2026-06-14"
    saat_baslangic = Column(String, nullable=False)  # Örn: "13:00"
    saat_bitis = Column(String, nullable=False)  # Örn: "15:00"

    # Opsiyonel not alanı (nullable=True)
    talep_not = Column(String, nullable=True)

    # Kaydın açıldığı anı otomatik damgalar
    olusturma_tarihi = Column(DateTime(timezone=True), server_default=func.now())