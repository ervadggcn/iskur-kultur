from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Veritabanı dosyamızın adı (Proje klasöründe otomatik oluşacak)
SQLALCHEMY_DATABASE_URL = "sqlite:///./kultur_merkezi.db"

# engine: Veritabanı ile aramızdaki ana motor
# check_same_thread=False ayarı, FastAPI'nin çoklu asenkron isteklerinde
# SQLite'ın çökmesini engellemek için kritik bir ayardır.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal: Her bir API isteği geldiğinde veritabanıyla konuşacak olan "oturum"
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base: Tüm veritabanı tablolarımızın (modellerimizin) miras alacağı temel sınıf
Base = declarative_base()