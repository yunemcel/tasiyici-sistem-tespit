---
date: 2026-09-03
time: "14:21"
timezone: Europe/Istanbul
agent: ChatGPT
model: GPT-5.6 Sol
role: standalone distribution + repository cleanup
status: completed
---

# Standalone dağıtım ve repository temizliği

## Yapılanlar

- Windows ve Android'de doğrudan dosya olarak açılabilen tek HTML dağıtımı eklendi.
- Tek HTML sürümünün modüler runtime'dan türetilmesi için `tools/build-standalone.py` eklendi.
- Runtime değişikliklerinde standalone dosyayı yeniden üreten GitHub Actions workflow'u eklendi.
- Workflow başarıyla çalıştırıldı ve `Tasiyici_Sistem_Tespit_Standalone.html` repository köküne üretildi.
- README, tasarım yönetmeliği, agent sözleşmesi, tasarım felsefesi, mimari doküman, changelog ve önceki agent kaydı başka ürün/repository karşılaştırmalarından arındırıldı.
- Manuel QA listesine Windows ve Android tek HTML senaryoları eklendi.

## Dağıtım kararı

İki resmi dağıtım biçimi vardır:

1. Modüler PWA: GitHub Pages/HTTPS, service worker ve kurulabilir web uygulaması için.
2. Standalone HTML: Windows ve Android'de kopyalanıp doğrudan açılabilen, CSS ve JavaScript'i kendi içinde taşıyan tek dosya için.

İki dağıtım ayrı ürün değildir. Aynı karar motoru, görünümler ve veri kuralları kullanılmalıdır.

## Veri notu

PWA origin'i ile `file://` üzerinden açılan standalone dosyanın localStorage alanı farklı olabilir. Cihazlar veya dağıtım biçimleri arasında kayıt taşımak için JSON dışa/içe aktarma kullanılmalıdır.

## QA

- Standalone build workflow job sonucu: success.
- Üretilen standalone dosya `main` dalında doğrulandı.
- Tek HTML içinde CSS gömülü olarak doğrulandı.
- Repository güncel kod aramasında kaldırılması istenen diğer ürün/repository ifadeleri için sonuç bulunmadı.
