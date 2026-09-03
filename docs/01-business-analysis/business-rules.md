# Business Rules

## BR-001 — Proje
Proje adı isteğe bağlıdır. Boşsa kayıt `Genel` projesine alınır.

## BR-002 — Analiz numarası
Analiz numarası isteğe bağlıdır. Boş bırakıldığında aynı proje içinde kullanılmayan ilk `Analiz_N` değeri atanır.

## BR-003 — Benzersizlik
Aynı cihaz arşivinde `proje + analiz numarası` ikilisi benzersiz olmalıdır.

## BR-004 — Bilinmeyen cevap
Boş veya `Bilmiyorum` cevap puan üretmez. Kullanıcı tahmine zorlanmaz.

## BR-005 — Minimum veri
Ayırt edici cevap sayısı 5'ten azsa veya en yüksek aday puanı 8'den düşükse sonuç `Sonuç için veri yetersiz` olur.

## BR-006 — Yakın aday
En yüksek iki aday arasındaki puan farkı 2 veya daha azsa sonuç iki aday arasında belirsiz gösterilir.

## BR-007 — Karma sistem
Kullanıcı bina bölümleri/katlar arasında açık farklı taşıyıcı sistem olduğunu bildirirse sonuç tek sınıfa zorlanmaz; `Karma taşıyıcı sistem olası` önceliklidir.

## BR-008 — Kayıt yeri
Analizler varsayılan olarak yalnız cihazın bu origin için ayrılmış `localStorage` alanında saklanır.

## BR-009 — Dışa aktarma
Dışa aktarma açık kullanıcı eylemidir. Tek analiz veya tüm arşiv JSON olarak üretilebilir.

## BR-010 — İçe aktarma / aynı kayıt
İçe gelen kayıt ID'si yerelde varsa `updatedAt` daha yeni olan sürüm tercih edilir.

## BR-011 — İçe aktarma / numara çakışması
Farklı ID'li kayıt aynı proje + analiz numarasıyla gelirse kayıt kaybedilmez; içe gelen kayda benzersiz yeni numara verilir.

## BR-012 — Hafızayı sil
“Analiz hafızasını sil” bu uygulamaya ait localStorage/tercih kayıtlarını kaldırır. Kullanıcının cihaz dosya sistemine dışa aktardığı JSON dosyalarını silemez.

## BR-013 — Resmî karar sınırı
Hiçbir sonuç deprem güvenliği, riskli yapı veya mühendislik performans kararı olarak etiketlenemez.
