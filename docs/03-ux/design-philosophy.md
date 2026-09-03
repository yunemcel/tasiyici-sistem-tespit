# Tasarım Felsefesi

Bu ürün sahada tek bir karar akışını hızlandıran operasyonel bir araçtır. Tasarımın görevi, çok sayıda gözlemi aynı yüzeyde okunabilir tutmak ve kullanıcının sonucu gereksiz navigasyon olmadan üretmesini sağlamaktır.

## Tutarlılık davranışta, kompozisyon görevde

Turuncu kimlik çizgisi, tipografi, border dili ve focus davranışı ürün içinde süreklilik kurar. Buna karşılık ekran geometrisi alışkanlıkla tekrar edilmez; 15 soruluk tespit formu, arşiv ve sonuç ekranı farklı görevleri çözdükleri için kompozisyonları görevden türetilir.

## Yüksek bilgi yoğunluğu burada doğaldır

Saha kullanıcısının aynı yapıya ilişkin soruları birlikte görmesi karşılaştırmayı kolaylaştırır. Beş ayrı sayfa arasında gidip gelmek görev hızını düşürür. Bu nedenle tek sayfa form bilinçli tercihtir.

## Renk karar değil işarettir

Turuncu primary action, kırmızı destructive, yeşil başarılı/yüksek güven işaretidir. Sonuç yalnız renkle anlatılmaz; başlık ve metin etiketi her zaman vardır.

## Minimalizm teknik bilgiyi saklamak değildir

Gereksiz shadow, kart ve dekorasyon çıkarılır; fakat “karma sistem”, “veri yetersiz”, “mühendislik sınırı” gibi kritik bilgi gizlenmez.

## Aynı işlev iki dağıtım biçiminde korunur

PWA sürümü HTTPS ve service worker üzerinden kurulabilir/çevrimdışı çalışabilir. Tek HTML sürümü ise Windows ve Android'de dosyanın doğrudan açılması için bütün CSS ve JavaScript'i kendi içinde taşır. İki dağıtım biçiminde karar motoru, arşiv ve veri aktarım davranışı aynı kalmalıdır.

## Mobil uygulama hissi, web davranışını bozmadan

PWA standalone modunda uygulama hissi hedeflenir. Buna rağmen platform-native dosya seçici, paylaşım sayfası, Safari Ana Ekrana Ekle ve erişilebilir focus davranışları korunur.
