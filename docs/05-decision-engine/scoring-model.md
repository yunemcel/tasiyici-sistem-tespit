# Decision Engine — Scoring Model

## Durum

Bu motor **uzman-heuristic** ağırlıklı kural sistemidir. Etiketli saha veri setiyle ampirik olarak kalibre edilmiş olasılık modeli değildir.

Amaç tek bir yanlış gözlemin sonucu kilitlemesini önlemek ve eksik veride belirsizliği korumaktır.

## Sınıflar

- Betonarme Karkas
- Çelik Karkas
- Yığma Kâgir
- Yığma Yarı Kâgir
- Ahşap
- Kerpiç
- Taş Duvarlı
- Basit Bina

## Ana puan kuralları

### İskelet

- Tekrarlayan karkas var: Betonarme +4, Çelik +4, Ahşap +2
- Karkas görünmüyor: Yığma +3, Yarı Kâgir +2, Kerpiç +2, Taş +2
- İskelet malzemesi betonarme: Betonarme +9
- Çelik profil: Çelik +8
- Ahşap: Ahşap +7, Yarı Kâgir +1
- Karma iskelet: Basit +2, Yarı Kâgir +2
- Sürekli bağımsız kolon: Betonarme +3, Çelik +3, Ahşap +2
- Kolon yok: Yığma +2, Kerpiç +1, Taş +1

### Duvar

- Kalın/sürekli taşıyıcı duvar: Yığma +5, Yarı Kâgir +4, Kerpiç +4, Taş +4
- Taşıyıcı duvar yok: Betonarme +2, Çelik +2, Ahşap +1
- Taş: Taş +7, Yığma +3, Yarı Kâgir +2
- Tuğla/briket/blok: Yığma +5, Yarı Kâgir +3; karkas görünüyorsa Betonarme +1
- Kerpiç/toprak: Kerpiç +10
- Ahşap çatkı: Ahşap +7
- Karma duvar: Basit +3, Yarı Kâgir +2
- Duvar 30–49 cm: Yığma/Yarı Kâgir/Kerpiç/Taş +2
- Duvar 50 cm+: Taş +3, Kerpiç +3, Yığma +2
- <20 cm ve taşıyıcı duvar işareti yok: Betonarme +1, Çelik +1
- Taş + çamur/toprak harç: Taş +6
- Taş + kireç/çimento harcı: Yığma +3

### Döşeme / yük aktarımı

- Betonarme döşeme: Betonarme +3, Yığma +2
- Ahşap döşeme: Yarı Kâgir +5, Ahşap +3, Taş +1
- Çelik döşeme: Çelik +3
- Karma döşeme: Yarı Kâgir +2, Basit +2
- Döşeme karkasa oturuyor: Betonarme +6, Çelik +5, Ahşap +3
- Döşeme duvara oturuyor: Yığma +7, Yarı Kâgir +5, Kerpiç +4, Taş +4
- Taşıyıcı duvar + duvara oturan betonarme döşeme: Yığma ek +6
- Taşıyıcı duvar + duvara oturan ahşap döşeme: Yarı Kâgir ek +7
- Geniş zemin kat açıklığı: Betonarme +2, Çelik +2

### Özel işaretler

- Çelik yalnız çatıda: Çelik toplamından 5 düşür
- Çelik karkasta da var ve çelik iskelet seçilmiş: Çelik +5
- Ahşap dikme/çapraz esas iskelet: Ahşap +9
- Ahşap iskelet yok + ahşap döşeme + taşıyıcı duvar: Yarı Kâgir +3
- Açık kerpiç blok: Kerpiç +10
- Duvar “kerpiç” seçilmiş ama açık blok görülmüyor: Kerpiç −2
- Basit/düşük standartlı karma yapı: Basit +10
- Basit yapı değil: Basit −2 (alt sınır 0)

## Birleşik güçlü kanıtlar

- Betonarme iskelet + sürekli kolon + döşeme karkasa: Betonarme ek +7
- Çelik iskelet + sürekli kolon + döşeme karkasa + çelik yalnız çatı değil: Çelik ek +7
- Taş + taşıyıcı duvar + döşeme duvara: Taş ek +5
- Tuğla + taşıyıcı duvar + döşeme duvara + betonarme döşeme: Yığma ek +5
- Taş/tuğla + taşıyıcı duvar + döşeme duvara + ahşap döşeme: Yarı Kâgir ek +5

## Çelişki kayıtları

Motor karkas + taşıyıcı duvar, döşeme karkasa + taşıyıcı duvar, belirgin RC/çelik kolon + döşeme duvara, yalnız çelik çatı ve kat/bölüm bazında farklı sistem gibi çelişkileri kullanıcıya ayrıca gösterir.

## Sonuç eşikleri

1. `mixedSystem = Evet` → `Karma taşıyıcı sistem olası`
2. ayırt edici cevap `< 5` veya top score `< 8` → `Sonuç için veri yetersiz`
3. top − second `<= 2` → iki aday arasında belirsiz
4. aksi halde top sınıf:
   - margin `>= 7` ve top `>= 15` → yüksek olasılıklı ön sınıflandırma
   - margin `>= 4` → orta olasılıklı
   - aksi → düşük olasılıklı

Bu “olasılık” etiketleri istatistiksel probability değildir; kural motoru içindeki kanıt ayrışma seviyesidir.

## Sonraki kontrol önerileri

- Betonarme vs Yığma: döşemenin karkasa mı duvara mı oturduğunu kontrol et
- Yığma vs Yarı Kâgir: döşeme altı/çatı arasında ahşap kiriş ara
- Taş vs Yığma: harç, kalınlık ve döşeme mesnetini kontrol et
- Betonarme vs Çelik: kolon/kiriş malzemesini doğrula; çelik çatı tek başına yeterli değil
- Ahşap vs Yarı Kâgir: ahşap iskeletin katlar boyunca ana taşıyıcı olup olmadığını belirle

## Gelecek kalibrasyon kuralı

Ağırlıklar yalnız sezgisel “daha iyi hissettirdiği” için değiştirilmemelidir. Mümkün olduğunda doğrulanmış örnekler, hata sınıfları ve saha geri bildirimi kaydedilmelidir.
