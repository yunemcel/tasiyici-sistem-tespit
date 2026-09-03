# Architecture — Offline Static PWA

## Sistem bağlamı

```text
Kullanıcı
  ↓
HTTPS / GitHub Pages
  ↓
index.html + app.css + app.js + manifest + service worker
  ↓
localStorage (analizler)
  ↕
JSON dosyası (manuel import/export)
```

Backend, API, auth sunucusu veya bulut veritabanı yoktur.

## Dosyalar

- `index.html`: statik uygulama kabuğu
- `app.css`: görsel sistem ve responsive davranış
- `app.js`: route, karar motoru ve yerel veri yönetimi
- `manifest.webmanifest`: PWA metadata
- `sw.js`: app-shell cache ve offline fallback
- `icon.svg`: PWA/favikon kaynağı
- `.nojekyll`: GitHub Pages statik yayın işareti

## Origin ve veri

`localStorage` origin'e bağlıdır. GitHub Pages adresi değişirse veya farklı host kullanılırsa kullanıcı yeni yerel veri alanı görür. Önemli saha kayıtları düzenli JSON dışa aktarma ile yedeklenmelidir.

## Service worker

Service worker `http://localhost` veya `https://` güvenli bağlamda çalışır. `file://` üzerinden PWA kurulumu hedeflenmez. App-shell değiştiğinde cache version yükseltilmelidir.

## GitHub Pages path

Repository project page olarak yayınlandığı için varlık yolları relative (`./...`) kalmalıdır. Root-absolute `/sw.js` kullanılmamalıdır.

## iOS

Hedef akış: Safari ile HTTPS sayfasını aç → Ana Ekrana Ekle → online ilk açılış → offline tekrar açılış. WhatsApp/Files Quick Look yerel HTML önizlemesi uygulama runtime'ı değildir.

## Veri kaybı riski

Tarayıcı/site verisi kullanıcı tarafından temizlenirse localStorage kayıtları silinebilir. Merkezi senkronizasyon olmadığı için JSON export yedekleme mekanizmasıdır.
