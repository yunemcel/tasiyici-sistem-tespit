# ADR-002 — JSON ile Cihazlar Arası Analiz Aktarımı

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-03

## Bağlam

Merkezi sunucu olmadan birden fazla saha cihazındaki analizlerin tek cihazda toplanması gerekmektedir.

## Karar

Analiz arşivi JSON dosyası olarak dışa/içe aktarılır.

## Birleştirme kuralları

- kayıt `id` alanı cihazlar arası kimliktir,
- aynı ID gelirse daha yeni `updatedAt` seçilir,
- farklı ID fakat aynı proje + analiz numarası çakışırsa içe gelen kayıt yeniden numaralanır,
- var olan diğer kayıtlar korunur.

## Neden JSON?

İnsan tarafından incelenebilir, platformlar arası taşınabilir, backend gerektirmez, iOS Files / Share Sheet ile paylaşılabilir ve ileride merkezi import pipeline'a dönüştürülebilir.

CSV ana değişim formatı seçilmedi; nested answer/result yapısı ve sürüm metadata'sı için JSON daha uygundur.
