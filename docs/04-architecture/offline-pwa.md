# Architecture — Offline Static PWA

## Sistem bağlamı

```text
Kullanıcı
  ↓
HTTPS / GitHub Pages
  ↓
index.html
  ├─ app.css
  ├─ engine.js
  ├─ core.js
  ├─ views.js
  └─ app.js
  ↓
localStorage (analizler)
  ↕
JSON dosyası (manuel import/export)

manifest.webmanifest + sw.js
  ↓
PWA metadata + app-shell offline cache
```

Backend, API, auth sunucusu veya bulut veritabanı yoktur.

## Runtime dosyaları

- `index.html`: statik uygulama kabuğu ve erişilebilir landmark'lar
- `app.css`: görsel sistem, responsive davranış ve focus kuralları
- `engine.js`: taşıyıcı sistem puanlama / sonuç motoru
- `core.js`: localStorage, route yardımcıları ve ortak state
- `views.js`: ana sayfa, tespit, arşiv, sonuç, referans ve yardım görünümleri
- `app.js`: form kontrolcüsü, modal, import/export, arama ve service worker kaydı
- `manifest.webmanifest`: PWA metadata
- `sw.js`: app-shell cache ve offline fallback
- `icon.svg`: PWA/favikon kaynağı
- `.nojekyll`: GitHub Pages statik yayın işareti

Karar motorunun ayrı dosyada tutulması bilinçlidir: UI değişiklikleri puanlama mantığına istemeden dokunmamalı; motor değişiklikleri de `docs/05-decision-engine/scoring-model.md` ile birlikte izlenebilmelidir.

## Origin ve veri

`localStorage` origin'e bağlıdır. GitHub Pages adresi değişirse veya farklı host kullanılırsa kullanıcı yeni yerel veri alanı görür. Önemli saha kayıtları düzenli JSON dışa aktarma ile yedeklenmelidir.

## Service worker

Service worker `http://localhost` veya `https://` güvenli bağlamda çalışır. `file://` üzerinden PWA kurulumu hedeflenmez. App-shell değiştiğinde cache version yükseltilmelidir.

Mevcut app-shell cache'i şunları içerir:

- `./`
- `./index.html`
- `./app.css`
- `./engine.js`
- `./core.js`
- `./views.js`
- `./app.js`
- `./manifest.webmanifest`
- `./icon.svg`

## GitHub Pages path

Repository project page olarak yayınlandığı için varlık yolları relative (`./...`) kalmalıdır. Root-absolute `/sw.js` veya `/app.js` kullanılmamalıdır.

## iOS

Hedef akış: Safari ile HTTPS sayfasını aç → Ana Ekrana Ekle → online ilk açılış → offline tekrar açılış. WhatsApp/Files Quick Look yerel HTML önizlemesi uygulama runtime'ı değildir.

## Veri kaybı riski

Tarayıcı/site verisi kullanıcı tarafından temizlenirse localStorage kayıtları silinebilir. Merkezi senkronizasyon olmadığı için JSON export yedekleme mekanizmasıdır.
