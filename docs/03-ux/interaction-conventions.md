# Interaction Conventions

## Navigasyon

- Hash route kullanılır; tarayıcı ileri/geri davranışı korunur.
- Yeni tespit tek uzun form yüzeyidir.
- Sonuç, arşiv, referans ve yardım ayrı route olabilir.

## Arama

Global arama yerel arşivde analiz numarası, proje, not ve sonuç başlığında arama yapar. Masaüstünde `Ctrl+K` / `Command+K` arama alanına focus verebilir; shortcut görsel kutu olarak yer kaplamak zorunda değildir.

## Modal

- dış backdrop tıklaması kapatır,
- `Escape` kapatır,
- Tab focus modal dışına kaçmaz,
- kapatınca focus tetikleyiciye döner,
- destructive işlem confirmation ister.

## Seçimler

- Radio control başka seçeneğe basılarak değiştirilebilir.
- “Bilmiyorum” geçerli cevaptır.
- Kullanıcı cevabı boş da bırakabilir.

## Focus

- Etkileşim kontrollerinde görünür focus korunur.
- Route değişiminde tüm `main` alanına focus çerçevesi çizilmez.

## Mobil veri paylaşımı

Dışa aktarmada öncelik: `navigator.share` + dosya paylaşımı destekleniyorsa sistem share sheet; desteklenmiyorsa Blob download. İçe aktarma standart `<input type=file>` üzerinden Files/Dosyalar seçicisini kullanır.

## Offline

İlk HTTPS açılışında service worker kaydolur. Kurulum sonrası kullanıcı online/offline durum fark etmeksizin aynı temel arayüzü görür.
