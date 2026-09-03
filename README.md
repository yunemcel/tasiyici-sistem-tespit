# Taşıyıcı Sistem Tespit

Saha gözlemlerinden **taşıyıcı sistem türü için ön sınıflandırma** üreten, yerel çalışan ve çevrimdışı kullanılabilen karar destek aracı.

Bu repository; uygulama kodu, karar motoru, veri kuralları, UX kararları ve teknik mimari için **source of truth** olarak kullanılır.

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

## Kullanım biçimleri

### 1. Tek HTML — Windows / Android

Repository kökündeki `Tasiyici_Sistem_Tespit_Standalone.html` dosyası bütün CSS ve JavaScript kodunu kendi içinde taşır.

- Windows'ta dosyaya çift tıklayıp Edge, Chrome veya Firefox ile açılabilir.
- Android'de HTML dosyasını JavaScript çalıştırabilen bir tarayıcıyla açabilirsiniz.
- İnternet bağlantısı gerekmez.
- Analiz arşivi tarayıcının yerel hafızasında tutulur.
- JSON dışa/içe aktarma kullanılabilir.

Bu dosya PWA kurulumu yapmaz; amacı tek dosyayı kopyalayıp doğrudan çalıştırmaktır.

### 2. PWA — iOS / Android / masaüstü

Modüler runtime GitHub Pages üzerinden HTTPS ile yayınlanır:

`https://yunemcel.github.io/tasiyici-sistem-tespit/`

iPhone/iPad için Safari → Paylaş → **Ana Ekrana Ekle** akışı kullanılmalıdır. Service worker online ilk açılıştan sonra uygulama kabuğunu cache'e alır ve sonraki açılışlarda çevrimdışı çalışma sağlar.

## GitHub Pages

Repository ayarında:

- **Source:** Deploy from a branch
- **Branch:** `main`
- **Folder:** `/ (root)`

seçilmelidir.

## Teknik özellikler

- statik HTML/CSS/JavaScript,
- yapay zekâ servisi yok,
- backend ve sunucu veritabanı yok,
- harici JavaScript/CDN bağımlılığı yok,
- analizler cihazın `localStorage` alanında tutulur,
- proje + analiz numarasıyla yerel arşiv,
- JSON dışa/içe aktarma,
- destekleyen mobil tarayıcılarda sistem paylaşım sayfası,
- PWA sürümünde service worker ile çevrimdışı kullanım.

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
- Dosya seçici üzerinden JSON içe aktarılabilir.
- Aynı kayıt kimliği tekrar gelirse daha yeni `updatedAt` tercih edilir.
- Aynı proje + analiz numarası çakışırsa içe gelen kayda benzersiz yeni analiz numarası verilir.

## Runtime yapısı

```text
index.html
  ├─ app.css      → responsive UI / tasarım sistemi
  ├─ engine.js    → karar motoru
  ├─ core.js      → localStorage / ortak state / yardımcılar
  ├─ views.js     → ekran görünümleri
  └─ app.js       → controller / import-export / modal / arama

manifest.webmanifest → PWA metadata
sw.js                 → offline app-shell cache
icon.svg              → uygulama ikonu / favicon

Tasiyici_Sistem_Tespit_Standalone.html
  └─ yukarıdaki runtime'ın tek dosyada gömülü dağıtımı
```

Karar motorunun UI'dan ayrı tutulması bilinçlidir. Puan değişiklikleri `docs/05-decision-engine/scoring-model.md` ile birlikte güncellenmelidir.

## Dokümantasyon

- [`AGENTS.md`](AGENTS.md) — agent çalışma sözleşmesi
- [`DESIGN.md`](DESIGN.md) — bağlayıcı görsel ve etkileşim kuralları
- [`docs/00-product/product-brief.md`](docs/00-product/product-brief.md) — ürün amacı ve kapsamı
- [`docs/01-business-analysis/business-rules.md`](docs/01-business-analysis/business-rules.md) — kayıt ve iş kuralları
- [`docs/02-domain-model/analysis-record.md`](docs/02-domain-model/analysis-record.md) — analiz kayıt modeli
- [`docs/03-ux/interaction-conventions.md`](docs/03-ux/interaction-conventions.md) — etkileşim davranışları
- [`docs/03-ux/design-philosophy.md`](docs/03-ux/design-philosophy.md) — tasarım gerekçesi
- [`docs/04-architecture/offline-pwa.md`](docs/04-architecture/offline-pwa.md) — çevrimdışı mimari
- [`docs/05-decision-engine/scoring-model.md`](docs/05-decision-engine/scoring-model.md) — karar motoru ve puanlar
- [`tests/manual-test-checklist.md`](tests/manual-test-checklist.md) — manuel QA listesi

## Tasarım dili

Arayüz; `CoFo Sans → Arial → Helvetica` font zinciri, turuncu ana vurgu, koyu nötr yüzeyler, kontrollü bilgi yoğunluğu, semantik renk, düşük dekorasyon, görünür klavye focus'u ve görevden türeyen kompozisyon kullanır.

Kullanıcıya dönük metinlerde kurumsal unvan, adres, telefon veya resmî ürün iddiası kullanılmaz.

## Çalışma yöntemi

Kalıcı ürün, UX, mimari ve karar motoru değişiklikleri yalnız sohbet geçmişinde bırakılmamalıdır. İlgili değişiklik `docs/`, `DESIGN.md`, ADR ve gerekiyorsa `agent-logs/` altına işlenmelidir.

## Lisans

Açık kaynak lisansı henüz seçilmemiştir. Repository'nin public olması tek başına yeniden kullanım veya yeniden lisanslama izni tanımlamaz.
