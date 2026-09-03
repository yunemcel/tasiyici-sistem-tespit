# ADR-001 — Local-first Statik PWA

- **Durum:** Kabul edildi
- **Tarih:** 2026-09-03

## Bağlam

Araç sahada iOS/Android ve masaüstünde kullanılmalı, internet bağlantısı kesildiğinde temel analiz akışı devam etmelidir. Yapay zekâ, backend veya kullanıcı hesabı gerekmemektedir.

## Karar

Uygulama statik PWA olarak tutulacaktır: HTML/CSS/JS istemci tarafı, GitHub Pages/HTTPS dağıtımı, service worker app-shell cache ve localStorage analiz arşivi.

## Sonuçlar

Olumlu: kurulum kolay, backend işletim maliyeti yok, saha offline çalışması mümkün, veri varsayılan olarak cihazda kalır.

Risk: cihaz/site verisi temizlenirse arşiv kaybolabilir, otomatik cihazlar arası senkronizasyon yoktur, iOS yerel `.html` dosyasından doğrudan PWA kurulamaz; HTTPS gerekir.

Bu riskler JSON dışa aktarma ve kullanıcı bilgilendirmesiyle yönetilir.
