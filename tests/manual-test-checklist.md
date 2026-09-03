# Manuel Test Kontrol Listesi

## Windows — tek HTML

- [ ] `Tasiyici_Sistem_Tespit_Standalone.html` dosyasına çift tıklayınca güncel tarayıcıda açılıyor
- [ ] Harici CSS/JS dosyası olmadan ana sayfa oluşuyor
- [ ] Yeni tespit formunda 15 soru aynı sayfada
- [ ] Analiz oluşturma → sonuç → arşiv zinciri çalışıyor
- [ ] Tarayıcı kapatılıp dosya tekrar açıldığında localStorage izin veriyorsa analiz duruyor
- [ ] JSON dışa aktarma çalışıyor
- [ ] JSON içe aktarma çalışıyor
- [ ] İnternet bağlantısı olmadan temel işlevler çalışıyor

## Masaüstü — PWA / GitHub Pages

- [ ] GitHub Pages adresi açılıyor
- [ ] Header tek satır ve arama kutusu çift border üretmiyor
- [ ] Sayfa açıldığında çalışma alanı çevresinde büyük siyah focus çerçevesi yok
- [ ] Yeni tespit formunda 15 soru aynı sayfada
- [ ] Boş analiz numarası otomatik `Analiz_1` oluyor
- [ ] Aynı projede ikinci kayıt `Analiz_2` oluyor
- [ ] Proje filtresi ve arama çalışıyor
- [ ] Sonuç kopyalama çalışıyor
- [ ] JSON dışa aktarma çalışıyor
- [ ] JSON içe aktarma çalışıyor
- [ ] Modal dış tıklama ve Escape ile kapanıyor
- [ ] Hafızayı sil bütün yerel analizleri kaldırıyor

## Karar motoru smoke test

- [ ] RC frame + RC material + columns + floor on frame → Betonarme Karkas güçlü aday
- [ ] thick brick bearing walls + RC floor on walls → Yığma Kâgir güçlü aday
- [ ] thick masonry walls + wood floor on walls → Yığma Yarı Kâgir güçlü aday
- [ ] visible adobe → Kerpiç güçlü aday
- [ ] stone bearing wall + mud mortar → Taş Duvarlı güçlü aday
- [ ] steel only at roof does not force Çelik Karkas
- [ ] mixedSystem=yes → Karma taşıyıcı sistem olası
- [ ] çok az cevap → Veri yetersiz

## iOS Safari / PWA

- [ ] HTTPS adresi Safari'de açılıyor
- [ ] Paylaş → Ana Ekrana Ekle çalışıyor
- [ ] Ana ekran ikonu/başlığı kullanılabilir
- [ ] Standalone açılışta UI taşmıyor
- [ ] Online ilk açılıştan sonra Uçak Modunda tekrar açılıyor
- [ ] Analiz kaydı uygulama yeniden açıldığında duruyor
- [ ] Paylaş / Dışa Aktar share sheet açıyor veya fallback download sağlıyor
- [ ] Dosyadan İçe Aktar Files seçicisini açıyor

## Android — PWA

- [ ] Chrome'da GitHub Pages adresi açılıyor
- [ ] install/PWA akışı çalışıyor
- [ ] offline tekrar açılış çalışıyor
- [ ] JSON paylaşım veya indirme çalışıyor

## Android — tek HTML

- [ ] `Tasiyici_Sistem_Tespit_Standalone.html` dosyası JavaScript çalıştıran tarayıcıda açılıyor
- [ ] 15 soruluk tespit ekranı çalışıyor
- [ ] Analiz arşivi oluşturulabiliyor
- [ ] JSON dışa/içe aktarma çalışıyor
- [ ] İnternet kapalıyken temel işlevler çalışıyor

## Dağıtım eşliği

- [ ] PWA ve standalone aynı 15 soruyu gösteriyor
- [ ] Aynı yanıt seti iki dağıtımda aynı ana sonucu üretiyor
- [ ] Runtime değişikliğinden sonra GitHub Actions standalone dosyayı yeniden üretiyor
