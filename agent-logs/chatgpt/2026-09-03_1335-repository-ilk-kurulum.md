---
date: 2026-09-03
time: "13:35"
timezone: Europe/Istanbul
agent: ChatGPT
model: GPT-5.6 Sol
role: repository bootstrap + PWA/documentation
status: completed
---

# Repository ilk kurulum

## İncelenenler

- `yunemcel/ari-portal` kök repository yapısı
- ARI Portal `README.md` ve `AGENTS.md`
- kullanıcı tarafından sağlanan ARI tasarım yönetmeliği ve tasarım felsefesi
- mevcut Taşıyıcı Sistem Tespit v3 PWA paketi

## Yapılanlar

- repository source-of-truth yaklaşımına göre yapılandırıldı,
- ürün kapsamı ve açık karar belgeleri eklendi,
- analiz domain modeli ve business rules yazıldı,
- ARI Portal tasarım ailesinden türetilmiş ürün-özel `DESIGN.md` oluşturuldu,
- PWA/local-first mimarisi ADR ile kaydedildi,
- JSON cihazlar arası aktarım kararı ADR olarak kaydedildi,
- karar motorunun mevcut heuristic puanları açıkça dokümante edildi,
- manuel masaüstü/iOS/Android QA kontrol listesi eklendi,
- PWA runtime repository köküne kuruldu,
- monolitik HTML yaklaşımı GitHub Pages için `index.html + app.css + engine.js + core.js + views.js + app.js` olarak ayrıldı,
- service worker bütün runtime modüllerini cache'e alacak biçimde `tasiyici-tespit-v5` sürümüne yükseltildi,
- relative asset yolları GitHub Pages project-site path'i için korundu,
- resmî ARI Şehircilik iletişim/unvan footer içeriği kullanılmadı.

## Runtime ayrımının gerekçesi

Karar motoru `engine.js` içinde UI'dan ayrıldı. Böylece ekran/UX değişikliği puanlama mantığına istemeden dokunmadan yapılabilir ve motor değişiklikleri `docs/05-decision-engine/scoring-model.md` ile birlikte takip edilebilir.

## QA

- `engine.js`, `core.js`, `views.js` ve `app.js` Node sözdizimi kontrolünden geçti.
- Repository'deki runtime dosyalarının Git blob SHA'ları yerelde kontrol edilen kaynaklarla karşılaştırıldı.
- Görünüm modeli 5 bölüm ve toplam 15 soru üretiyor.
- Karar motoru smoke testlerinde Betonarme Karkas, Yığma Kâgir, Yığma Yarı Kâgir, Kerpiç, Taş Duvarlı ve Karma taşıyıcı sistem senaryoları beklenen ana sonucu verdi.
- Çalışma ortamının tarayıcı güvenlik politikası localhost/file URL navigasyonunu engellediği için gerçek Chromium tıklama testi bu oturumda tamamlanamadı. Bunun yerine sözdizimi, görünüm üretimi, blob eşleşmesi ve karar motoru testleri uygulandı.

## Bilinçli uyarlamalar

ARI Portal'ın çok modüllü ürün belgeleri bu küçük araca aynen kopyalanmadı. Aynı repository disiplini korundu; yalnız ürünün gerçekten ihtiyaç duyduğu product, business rule, domain, UX, architecture, decision-engine, ADR ve QA katmanları oluşturuldu.

## Açık işler

- GitHub Pages repository ayarının kullanıcı tarafından `main / (root)` olarak etkinleştirilmesi,
- canlı Pages URL üzerinde iOS Safari Ana Ekrana Ekle + offline QA,
- karar motorunun doğrulanmış saha örnekleriyle ileride kalibre edilmesi,
- iOS Ana Ekran ikonu için gerekirse ayrıca PNG touch-icon eklenmesi.
