# Taşıyıcı Sistem Tespit

Saha gözlemlerinden **taşıyıcı sistem türü için ön sınıflandırma** üreten, yerel çalışan ve çevrimdışı kullanılabilen karar destek aracı.

Bu repository; uygulama kodu, karar motoru, veri kuralları, UX kararları ve teknik mimari için **source of truth** olarak kullanılır. Repository disiplini `yunemcel/ari-portal` yaklaşımını örnek alır; ancak bu araç bağımsız ve küçük bir ürün olduğu için yalnız ihtiyacı olan dokümantasyon katmanlarını taşır.

> **Durum:** Yunus Emre Çelik tarafından çalışma arkadaşlarına karar desteği sağlamak amacıyla hobi olarak hazırlanmıştır. Resmî kurumsal uygulama değildir.

## Uygulama ne yapar?

Araç şu taşıyıcı sistem aileleri için gözlemsel ön sınıflandırma üretir:

- Betonarme Karkas
- Çelik Karkas
- Yığma Kâgir
- Yığma Yarı Kâgir
- Ahşap
- Kerpiç
- Taş Duvarlı
- Basit Bina

Tek bir gözleme göre karar vermez. Kolon-kiriş iskeleti, taşıyıcı duvar sürekliliği, döşemenin neye oturduğu, malzeme ve karma sistem işaretlerini birlikte puanlar. Veri yetersiz veya iki aday birbirine yakınsa sonuç kesinleştirilmez.

## Ne yapmaz?

Sonuç **deprem güvenliği**, **riskli yapı tespiti**, **performans analizi**, statik proje kontrolü veya mühendislik raporu değildir. Puanlar yalnızca bu karar motorundaki gözlemsel kanıt ağırlığıdır.

## Teknik özellikler

- Statik HTML/CSS/JavaScript PWA
- Yapay zekâ servisi yok
- Backend ve sunucu veritabanı yok
- Harici JavaScript/CDN bağımlılığı yok
- Analizler cihazın `localStorage` alanında tutulur
- Proje + analiz numarasıyla yerel arşiv
- JSON dışa/içe aktarma
- Mobil paylaşım sayfası desteği bulunan tarayıcılarda paylaşım
- Service worker ile çevrimdışı kullanım
- iOS Safari Ana Ekran PWA, Android ve masaüstü web hedefi

## Canlı kullanım — GitHub Pages

Repository kökten GitHub Pages ile yayınlanacak şekilde hazırlanmıştır.

GitHub repository ayarında:

- **Source:** Deploy from a branch
- **Branch:** `main`
- **Folder:** `/ (root)`

seçilmelidir.

Beklenen adres:

`https://yunemcel.github.io/tasiyici-sistem-tespit/`

### iPhone / iPad

1. Yukarıdaki HTTPS adresini **Safari** ile açın.
2. Safari paylaşım menüsünden **Ana Ekrana Ekle** seçeneğini kullanın.
3. Uygulamayı internet bağlantısı varken en az bir kez açın.
4. Service worker uygulama kabuğunu cache'e aldıktan sonra uygulama çevrimdışı açılabilir.

WhatsApp veya Files içindeki yerel `.html` dosyasını açmak PWA kurulumu değildir; iOS yerel dosya önizlemesinde JavaScript uygulama davranışı güvenilir değildir.

## Masaüstünde yerel geliştirme

Service worker için `file://` yerine HTTP kullanın. Python bulunan bir bilgisayarda:

```bash
python -m http.server 8080
```

Ardından `http://localhost:8080/` adresini açın.

## Analiz kayıtları

Her kayıt en az şu alanları taşır:

- benzersiz kayıt kimliği,
- proje adı,
- analiz numarası,
- isteğe bağlı saha notu,
- 15 sorunun yanıtları,
- hesaplanan sıralama ve güven seviyesi,
- oluşturulma ve güncellenme zamanı.

Analiz numarası boş bırakılırsa proje içinde `Analiz_1`, `Analiz_2`, ... biçiminde otomatik atanır.

## İçe / dışa aktarma

- Tüm arşiv veya tek analiz JSON olarak dışa aktarılabilir.
- Destekleyen mobil tarayıcılarda sistem paylaşım sayfası açılır.
- Dosyalar uygulamasından JSON seçilerek içe aktarma yapılabilir.
- Aynı kayıt kimliği tekrar gelirse daha yeni `updatedAt` tercih edilir.
- Aynı proje + analiz numarası çakışırsa içe gelen kayda benzersiz yeni analiz numarası verilir.

## Repository yapısı

```text
.
├── index.html
├── manifest.webmanifest
├── sw.js
├── icon-180.png
├── icon-512.png
├── .nojekyll
├── README.md
├── AGENTS.md
├── DESIGN.md
├── CHANGELOG.md
├── docs/
│   ├── 00-product/
│   ├── 01-business-analysis/
│   ├── 02-domain-model/
│   ├── 03-ux/
│   ├── 04-architecture/
│   ├── 05-decision-engine/
│   └── adr/
├── tests/
└── agent-logs/
    └── chatgpt/
```

## Dokümantasyon

- [`AGENTS.md`](AGENTS.md) — agent çalışma sözleşmesi
- [`DESIGN.md`](DESIGN.md) — bağlayıcı görsel ve etkileşim kuralları
- [`docs/00-product/product-brief.md`](docs/00-product/product-brief.md) — ürün amacı ve kapsamı
- [`docs/00-product/open-decisions.md`](docs/00-product/open-decisions.md) — açık kararlar
- [`docs/01-business-analysis/business-rules.md`](docs/01-business-analysis/business-rules.md) — kayıt ve iş kuralları
- [`docs/02-domain-model/analysis-record.md`](docs/02-domain-model/analysis-record.md) — analiz kayıt modeli
- [`docs/03-ux/interaction-conventions.md`](docs/03-ux/interaction-conventions.md) — etkileşim davranışları
- [`docs/03-ux/design-philosophy.md`](docs/03-ux/design-philosophy.md) — tasarım gerekçesi
- [`docs/04-architecture/offline-pwa.md`](docs/04-architecture/offline-pwa.md) — çevrimdışı/PWA mimarisi
- [`docs/05-decision-engine/scoring-model.md`](docs/05-decision-engine/scoring-model.md) — karar motoru ve puanlar
- [`docs/adr/ADR-001-local-first-static-pwa.md`](docs/adr/ADR-001-local-first-static-pwa.md)
- [`docs/adr/ADR-002-json-import-export.md`](docs/adr/ADR-002-json-import-export.md)
- [`tests/manual-test-checklist.md`](tests/manual-test-checklist.md) — manuel QA listesi

## Tasarım ailesi

Ürün, ARI Portal ile aynı tasarım ailesinin temel token ve davranış ilkelerini kullanır: `CoFo Sans → Arial → Helvetica`, ARI Orange / ARI Black temeli, kontrollü yoğunluk, semantik renk, düşük dekorasyon, görünür klavye focus'u ve görevden türeyen kompozisyon.

Bu görsel akrabalık ürünün resmî ARI Şehircilik uygulaması olduğu anlamına gelmez. Kullanıcıya dönük metinlerde kurumsal unvan, adres, telefon veya resmî ürün iddiası kullanılmaz.

## Çalışma yöntemi

Kalıcı ürün, UX, mimari ve karar motoru değişiklikleri yalnız sohbet geçmişinde bırakılmamalıdır. İlgili değişiklik `docs/`, `DESIGN.md`, ADR ve gerekiyorsa `agent-logs/` altına işlenmelidir.

## Lisans

Açık kaynak lisansı henüz seçilmemiştir. Repository'nin public olması tek başına yeniden kullanım veya yeniden lisanslama izni tanımlamaz.
