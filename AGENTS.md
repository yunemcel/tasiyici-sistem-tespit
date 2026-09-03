# AGENTS.md — Taşıyıcı Sistem Tespit Agent Çalışma Sözleşmesi

Bu repository ürün, karar motoru, UX ve teknik kararlar için source of truth'tur. Kalıcı kararlar sohbet geçmişine bırakılmaz.

## 1. Başlamadan önce

Göreve göre en az şu belgeleri oku:

1. `README.md`
2. ilgili `docs/` belgesi
3. UI/web/PWA değişikliği varsa `DESIGN.md`
4. yeni kompozisyon veya UX kararı gerekiyorsa `docs/03-ux/design-philosophy.md`
5. karar motoru etkileniyorsa `docs/05-decision-engine/scoring-model.md`
6. mimari karar etkileniyorsa ilgili ADR

## 2. Kaynak önceliği

Çelişki olduğunda sıra:

1. kullanıcının güncel ve açık talimatı,
2. kabul edilmiş ürün/business/UX/ADR kararı,
3. `DESIGN.md`,
4. ilgili `docs/` belgeleri,
5. mevcut çalışan ürün davranışı,
6. agent logları.

Agent logu tarihçedir; güncel ürün gerçeğinin yerine geçmez.

## 3. Ürün sınırı

- Araç gözlemsel taşıyıcı sistem ön sınıflandırması yapar.
- Deprem güvenliği, riskli yapı kararı veya mühendislik performans analizi yaptığı izlenimi oluşturma.
- Puanları bilimsel olasılık veya kalibre edilmiş güven skoru olarak adlandırma.
- Karar motoru ağırlıkları uzman-heuristic kurallardır; ampirik olarak kalibre edilmiş model değildir.
- Belirsizliği zorla tek sonuca dönüştürme.
- Karma sistem işaretini tek sınıf altında gizleme.

## 4. Local-first veri ilkesi

- Analiz verisi varsayılan olarak cihazdan çıkmaz.
- Backend, analytics, telemetry, reklam SDK'sı veya yapay zekâ servisi kullanıcı kararı olmadan eklenmez.
- İçe/dışa aktarma kullanıcı eylemiyle yapılır.
- Yerel hafızayı silme davranışı bu uygulamaya ait kayıtları gerçekten temizlemelidir.

## 5. Tasarım görevi

- `DESIGN.md` bağlayıcıdır.
- ARI Portal ile aynı tasarım ailesini koru; ekran geometrisini körlemesine kopyalama.
- Global shell çalışma yüzeyinden daha baskın olmamalıdır.
- Renk anlam taşır; dekoratif çeşitlilik için ek renk üretme.
- Her şeyi karta dönüştürme; bölüm, divider, tablo ve düz yüzeyleri kullan.
- Hover, focus, selected ve active durumlarını birbirine karıştırma.
- Focus göstergesini tüm sayfa konteynerine uygulama; gerçek etkileşim hedeflerinde göster.
- Mobilde yeterli dokunma hedefi ve görünür form label'ı koru.
- `prefers-reduced-motion` desteğini bozma.

## 6. PWA değişikliği

App shell değiştiğinde:

1. `sw.js` cache adını gerektiğinde yükselt,
2. GitHub Pages project path'i için relative yolları koru,
3. online ilk açılış + offline ikinci açılış senaryosunu test et,
4. iOS Safari Ana Ekrana Ekle akışını manuel QA listesine göre kontrol et.

## 7. Karar motoru değişikliği

Puanlar değişirse aynı çalışmada `docs/05-decision-engine/scoring-model.md` de güncellenir. Yeni ağırlığın gerekçesi, çelişki etkisi ve sonuç eşikleri açıkça yazılır.

## 8. Agent kaydı

Önemli ürün, tasarım, mimari veya karar motoru değişikliğinde `agent-logs/<agent>/YYYY-MM-DD_HHMM-kisa-konu.md` formatında tarihçeli kayıt bırak.

## 9. Yazım

- Türkçe karakterleri koru.
- Teknik ve doğrudan anlatım kullan.
- Jenerik yapay zekâ pazarlama dili kullanma.
- Mevcut gerçek, öneri ve açık kararı birbirine karıştırma.
