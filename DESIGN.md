---
project: Taşıyıcı Sistem Tespit
scope: web, PWA, standalone HTML, responsive UI
schema_version: 2
status: binding
updated: 2026-09-03
---

# DESIGN.md — Taşıyıcı Sistem Tespit Tasarım Yönetmeliği

Bu belge uygulamanın arayüzü, PWA yüzeyi ve tek HTML dağıtımı için bağlayıcı tasarım kurallarını tanımlar.

## 1. Öncelik sırası

1. işlev, okunabilirlik, güvenlik ve erişilebilirlik,
2. doğru içerik semantiği,
3. saha görev akışı ve karar hızı,
4. oran, boşluk, hizalama ve grid,
5. platform-native davranış,
6. renk ve tipografi tokenları,
7. dekorasyon.

## 2. Birincil görev

Kullanıcı mümkün olduğunca az navigasyonla gözlemleri işaretlemeli, analizi kaydetmeli ve gerektiğinde eski analizlere ulaşmalıdır.

- 15 soru tek tespit yüzeyinde tutulur.
- gereksiz wizard/çok adımlı sayfa geçişi kullanılmaz.
- sonuç sayfası ayrı olabilir; görev veri girişinden yorum/incelemeye geçer.
- arşiv tablo/liste yapısında sunulur.

## 3. Yüzey ve grid

- Ana çalışma genişliği en fazla yaklaşık `1440px`.
- Masaüstünde dış padding yaklaşık `28–38px` ailesinde.
- Mobilde güvenli içerik boşluğu yaklaşık `14–20px`.
- Global shell ve içerik başlangıçları aynı keyline ailesinde.
- Yoğun form ekranında anlamsız büyük boşluk üretilmez.

## 4. Tipografi

`"CoFo Sans", Arial, Helvetica, sans-serif`

- başlıklar kısa ve adlandırıcı,
- açıklamalar problem → gerekçe → sonuç ilişkisiyle,
- uzun UI metinleri sola hizalı,
- uppercase yalnız kısa eyebrow/kategori etiketlerinde.

## 5. Kök renkler

| Token | Değer | Rol |
|---|---|---|
| `accentOrange` | `#F8B231` | ana vurgu / primary action |
| `inkBlack` | `#3B3835` | koyu metin / seçili kontrol / footer |
| `errorRed` | `#B52E2C` | destructive / hata |
| `textPrimary` | `#333333` | ana metin |
| `backgroundWarm` | `#F8EFE4` | sakin açıklama yüzeyi |
| `surfaceMuted` | `#F1F1EE` | ikincil yüzey |
| `border` | `#D8D5D0` | standart sınır |
| `borderSubtle` | `#E8E6E2` | düşük ağırlıklı divider |
| `success` | `#2F7D4B` | başarılı/erişilebilir durum |
| `warning` | `#A96500` | dikkat / düşük güven |

Turuncu vurgu üzerinde standart boy beyaz metin kullanılmaz.

## 6. Header

- solda turuncu düşey kimlik çizgisi,
- ürün adı sakin ve ikincil,
- ortada arşiv araması,
- sağda sınırlı ana navigasyon/ayar eylemleri.

Header çalışma yüzeyinden daha baskın olmamalıdır. Arama kutusu tek dış sınır üretir; iç input ikinci border oluşturmaz. Klavye shortcut etiketi alanı sıkıştırmamalıdır.

## 7. Form ve seçimler

- Label görünürdür; placeholder label yerine geçmez.
- Radio seçimler yalnız renk ile değil dolu yüzey/kontrastla seçili durumu gösterir.
- “Bilmiyorum” meşru ve kolay erişilen cevaptır.
- Boş soru sistemde bilinmiyor kabul edilir.
- Mobil dokunma hedefleri yaklaşık 44 px çevresinde korunur.

## 8. Focus ve erişilebilirlik

Hedef WCAG 2.2 AA'dır.

- klavye focus'u gerçek etkileşim kontrolünde görünür,
- `main` veya bütün sayfa konteynerine route değişti diye büyük focus çerçevesi verilmez,
- modal focus trap ve `Escape` davranışı korunur,
- modal dış tıklama kapatır; destructive işlem confirmation ister,
- renk tek bilgi kanalı değildir,
- `prefers-reduced-motion` desteklenir.

## 9. Kart/panel

- Her soru ayrı rounded card değildir.
- Soru grupları section + divider + typography ile kurulur.
- Kart yalnız gerçekten ayrı bağlam gerektiğinde kullanılır.
- Büyük radius, ağır shadow ve glassmorphism tasarım dili değildir.

## 10. Arşiv

- Arşiv masaüstünde tablo, mobilde gerektiğinde yatay scroll ile çalışabilir.
- Proje, analiz numarası, sonuç ve güncelleme zamanı hızlı taranabilir olmalıdır.
- Silme normal primary action gibi görünmez.
- İçe/dışa aktarma açık etiketlenir.

## 11. Sonuç

- Birinci aday kadar belirsizlik de görünürdür.
- Güven etiketi mühendislik güvenlik derecesi gibi tasarlanmamalıdır.
- Karma sonuç tek sınıfa zorlanmaz.
- “Bir sonraki en değerli kontrol” sonucu tamamlayan saha eylemidir.

## 12. Footer

- resmî şirket iletişim/unvan bilgileri kullanılmaz,
- araç resmî kurumsal uygulama gibi sunulmaz,
- Yunus Emre Çelik tarafından çalışma arkadaşlarına hobi/karar destek amacıyla hazırlandığı belirtilebilir,
- mühendislik sınırı görünür kalır.

## 13. Responsive / dağıtım

- Reflow önceliklidir; sabit yükseklikten kaçınılır.
- Masaüstü iki kolonlu soru yüzeyi mobilde tek kolona iner.
- iOS standalone viewport davranışı bozulmamalıdır.
- PWA ve tek HTML sürümü aynı işlevsel UI'yı taşımalıdır.
- Tek HTML sürümünde harici CSS/JS bağımlılığı bulunmamalıdır.

## 14. QA

Final kabulünden önce arama çift border, büyük siyah focus çerçevesi, radio durumları, modal dış tıklama/Escape, 320–390 px taşma, iOS standalone, Windows/Android tek HTML, offline ikinci açılış, JSON import/export ve resmî ürün izlenimi kontrolleri yapılır.
