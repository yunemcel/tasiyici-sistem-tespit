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
- manuel masaüstü/iOS/Android QA kontrol listesi eklendi.

## Bilinçli uyarlamalar

ARI Portal'ın çok modüllü ürün belgeleri bu küçük araca aynen kopyalanmadı. Aynı repository disiplini korundu; yalnız ürünün gerçekten ihtiyaç duyduğu product, business rule, UX, architecture, decision-engine ve ADR katmanları oluşturuldu.

## Açık işler

- GitHub Pages repository ayarının etkinleştirilmesi/doğrulanması,
- canlı Pages URL üzerinde iOS Safari install + offline QA,
- karar motorunun doğrulanmış saha örnekleriyle ileride kalibre edilmesi.
