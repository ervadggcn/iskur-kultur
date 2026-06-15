# BUÜ Kültür Merkezi Randevu Yönetim Sistemi

Bursa Uludağ Üniversitesi Kültür Merkezi salonları (Mete Cengiz Salonu, Kırmızı Salon, Mavi Salon vb.) için geliştirilmiş, modern arayüze sahip tam kapsamlı bir randevu ve takvim yönetim sistemidir. 

Proje, arka planda **FastAPI** ve veritabanı yönetimi ile sağlam bir mimari sunarken, ön yüzde **FullCalendar** ve **Bootstrap 5** ile kullanıcı dostu, dinamik bir deneyim sağlar.

## 🚀 Özellikler

- **Dinamik Takvim Yönetimi:** Randevular haftalık veya aylık takvim üzerinde görselleştirilir. Sürükle-bırak veya form üzerinden saat seçimi yapılabilir.
- **Akıllı Çakışma Kontrolü (Collision Detection):** Aynı salon için kesişen saat aralıklarında mükerrer randevu oluşturulması sistem tarafından engellenir.
- **Tam CRUD İşlevselliği:** Takvim üzerindeki randevulara tıklanarak açılan modern Modal penceresi üzerinden randevu detayları görüntülenebilir, güncellenebilir (PUT) veya iptal edilebilir (DELETE).
- **Kurumsal İş Kuralları:** - Randevular sadece 08:00 - 22:00 saatleri arasında alınabilir.
  - Sadece tam saatlik (Örn: 10:00 - 13:00) periyotlara izin verilir, buçuklu saatler engellenmiştir.
- **Responsive & Modern Tasarım:** Uludağ Üniversitesi kurumsal kimliğine (renk paleti ve ikonlar) uygun, her ekranda sorunsuz çalışan modern arayüz.

## 🛠️ Kullanılan Teknolojiler

**Backend:**
- [Python 3.x](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) (Hızlı ve asenkron REST API mimarisi)
- [SQLAlchemy](https://www.sqlalchemy.org/) (ORM - Veritabanı işlemleri)
- [SQLite](https://www.sqlite.org/) (Yerleşik veritabanı)
- [Uvicorn](https://www.uvicorn.org/) (ASGI Sunucusu)

**Frontend:**
- HTML5, CSS3, JavaScript (ES6+)
- [Bootstrap 5](https://getbootstrap.com/) (UI Bileşenleri ve Modal yapısı)
- [FullCalendar.js](https://fullcalendar.io/) (Etkileşimli takvim modülü)
- [FontAwesome](https://fontawesome.com/) (İkon seti)

## 📁 Proje Yapısı

```text
├── assets/
│   ├── theme.css       # Özelleştirilmiş kurumsal UI stilleri
│   └── logo.png        # Üniversite / Proje logoları
├── database.py         # Veritabanı bağlantı ve oturum (session) ayarları
├── models.py           # SQLAlchemy veritabanı tablo şemaları
├── main.py             # FastAPI uygulaması, API uç noktaları (Endpoints)
├── index.html          # Tek sayfa (SPA) mimarisindeki ana arayüz
└── README.md           # Proje dökümantasyonu

⚙️ Kurulum ve Çalıştırma
Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Gerekli kütüphaneleri yükleyin:
Proje dizininde bir terminal açın ve gerekli Python paketlerini kurun:

Bash
pip install fastapi uvicorn sqlalchemy
2. Sunucuyu başlatın:
Aşağıdaki komut ile FastAPI sunucusunu ayağa kaldırın:

Bash
uvicorn main:app --reload
3. Uygulamaya Erişin:
Tarayıcınızı açın ve aşağıdaki adrese gidin:

Plaintext
[http://127.0.0.1:8000](http://127.0.0.1:8000)
🔌 API Uç Noktaları (Endpoints)
Sistem arka planda aşağıdaki RESTful API uç noktaları ile haberleşir:

GET / : Ana makine üzerinden index.html dosyasını sunar.

GET /api/randevular/{bina_adi} : Belirtilen binaya ait tüm randevuları getirir.

POST /api/randevu : İş kurallarını (çakışma, mesai saatleri) denetleyerek yeni randevu oluşturur.

PUT /api/randevu/{randevu_id} : Mevcut bir randevunun bilgilerini (saat, not, başvuran vb.) günceller.

DELETE /api/randevu/{randevu_id} : Seçilen randevuyu veritabanından kalıcı olarak siler.

Bu sistem, salon tahsis süreçlerini dijitalleştirmek, hızlandırmak ve insan kaynaklı planlama hatalarını sıfıra indirmek amacıyla tasarlanmıştır.

Bu harika projeyi tamamladığına göre, artık onu hem GitHub profilinde profesyonelce sergilemek hem de projeyi inceleyecek olan hocaların veya diğer geliştiricilerin sistemin nasıl çalıştığını ilk bakışta anlamasını sağlamak için sağlam bir `README.md` dosyasına ihtiyacın var.

Projenin tüm özelliklerini, iş kurallarını (çakışma kontrolü, mesai saatleri vb.) ve mimarisini özetleyen, donanım gereksinimleri gibi gereksiz detaylardan arındırılmış, doğrudan yazılım mimarisine odaklanan şık ve akademik/profesyonel bir README şablonunu aşağıda bulabilirsin.

Bunu `README.md` adında bir dosya oluşturup içine yapıştırabilirsin:

```markdown
# BUÜ Kültür Merkezi Randevu Yönetim Sistemi

Bursa Uludağ Üniversitesi Kültür Merkezi salonları (Mete Cengiz Salonu, Kırmızı Salon, Mavi Salon vb.) için geliştirilmiş, modern arayüze sahip tam kapsamlı bir randevu ve takvim yönetim sistemidir. 

Proje, arka planda **FastAPI** ve veritabanı yönetimi ile sağlam bir mimari sunarken, ön yüzde **FullCalendar** ve **Bootstrap 5** ile kullanıcı dostu, dinamik bir deneyim sağlar.

## 🚀 Özellikler

- **Dinamik Takvim Yönetimi:** Randevular haftalık veya aylık takvim üzerinde görselleştirilir. Sürükle-bırak veya form üzerinden saat seçimi yapılabilir.
- **Akıllı Çakışma Kontrolü (Collision Detection):** Aynı salon için kesişen saat aralıklarında mükerrer randevu oluşturulması sistem tarafından engellenir.
- **Tam CRUD İşlevselliği:** Takvim üzerindeki randevulara tıklanarak açılan modern Modal penceresi üzerinden randevu detayları görüntülenebilir, güncellenebilir (PUT) veya iptal edilebilir (DELETE).
- **Kurumsal İş Kuralları:** - Randevular sadece 08:00 - 22:00 saatleri arasında alınabilir.
  - Sadece tam saatlik (Örn: 10:00 - 13:00) periyotlara izin verilir, buçuklu saatler engellenmiştir.
- **Responsive & Modern Tasarım:** Uludağ Üniversitesi kurumsal kimliğine (renk paleti ve ikonlar) uygun, her ekranda sorunsuz çalışan modern arayüz.

## 🛠️ Kullanılan Teknolojiler

**Backend:**
- [Python 3.x](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) (Hızlı ve asenkron REST API mimarisi)
- [SQLAlchemy](https://www.sqlalchemy.org/) (ORM - Veritabanı işlemleri)
- [SQLite](https://www.sqlite.org/) (Yerleşik veritabanı)
- [Uvicorn](https://www.uvicorn.org/) (ASGI Sunucusu)

**Frontend:**
- HTML5, CSS3, JavaScript (ES6+)
- [Bootstrap 5](https://getbootstrap.com/) (UI Bileşenleri ve Modal yapısı)
- [FullCalendar.js](https://fullcalendar.io/) (Etkileşimli takvim modülü)
- [FontAwesome](https://fontawesome.com/) (İkon seti)

## 📁 Proje Yapısı

```text
├── assets/
│   ├── theme.css       # Özelleştirilmiş kurumsal UI stilleri
│   └── logo.png        # Üniversite / Proje logoları
├── database.py         # Veritabanı bağlantı ve oturum (session) ayarları
├── models.py           # SQLAlchemy veritabanı tablo şemaları
├── main.py             # FastAPI uygulaması, API uç noktaları (Endpoints)
├── index.html          # Tek sayfa (SPA) mimarisindeki ana arayüz
└── README.md           # Proje dökümantasyonu

```

## ⚙️ Kurulum ve Çalıştırma

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

**1. Gerekli kütüphaneleri yükleyin:**
Proje dizininde bir terminal açın ve gerekli Python paketlerini kurun:

```bash
pip install fastapi uvicorn sqlalchemy

```

**2. Sunucuyu başlatın:**
Aşağıdaki komut ile FastAPI sunucusunu ayağa kaldırın:

```bash
uvicorn main:app --reload

```

**3. Uygulamaya Erişin:**
Tarayıcınızı açın ve aşağıdaki adrese gidin:

```text
[http://127.0.0.1:8000](http://127.0.0.1:8000)

```

## 🔌 API Uç Noktaları (Endpoints)

Sistem arka planda aşağıdaki RESTful API uç noktaları ile haberleşir:

* `GET /` : Ana makine üzerinden `index.html` dosyasını sunar.
* `GET /api/randevular/{bina_adi}` : Belirtilen binaya ait tüm randevuları getirir.
* `POST /api/randevu` : İş kurallarını (çakışma, mesai saatleri) denetleyerek yeni randevu oluşturur.
* `PUT /api/randevu/{randevu_id}` : Mevcut bir randevunun bilgilerini (saat, not, başvuran vb.) günceller.
* `DELETE /api/randevu/{randevu_id}` : Seçilen randevuyu veritabanından kalıcı olarak siler.

