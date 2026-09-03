# Domain Model — AnalysisRecord

Uygulama backend kullanmadığı için model JavaScript nesnesi ve JSON export biçimi üzerinden yaşar.

## AnalysisRecord

```text
AnalysisRecord
- id: string
- project: string
- analysisNo: string
- note: string
- answers: AnswerSet
- result: AnalysisResult
- createdAt: ISO-8601 string
- updatedAt: ISO-8601 string
```

## AnswerSet

15 soru anahtarından oluşur:

```text
frame
frameMat
columns
bearingWalls
wallMat
wallThick
floor
floorSupport
wideOpen
steelRoofOnly
woodFrame
adobeVisible
stoneMortar
simple
mixedSystem
```

`u` değeri bilinmiyor/anlaşılamıyor anlamındadır.

## AnalysisResult

```text
AnalysisResult
- scores: Map<SystemClass, number>
- ranked: [SystemClass, number][]
- answered: number
- margin: number
- headline: string
- confidence: string
- level: high | medium | low | ambiguous | mixed
- evidence: string[]
- conflicts: string[]
- nextCheck: string
```

`id` cihazlar arası export/import sırasında aynı kaydın sürümlerini ayırt etmek için kullanılır. Uygun tarayıcıda `crypto.randomUUID()`, aksi halde zaman + rastgele parça kullanılır.
