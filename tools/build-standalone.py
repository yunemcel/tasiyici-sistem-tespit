from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
OUTPUT = ROOT / "Tasiyici_Sistem_Tespit_Standalone.html"

html = INDEX.read_text(encoding="utf-8")
css = (ROOT / "app.css").read_text(encoding="utf-8")

# PWA/harici asset referansları tek dosya dağıtımında gerekli değildir.
for tag in (
    '  <link rel="manifest" href="./manifest.webmanifest">\n',
    '  <link rel="icon" href="./icon.svg" type="image/svg+xml">\n',
    '  <link rel="apple-touch-icon" href="./icon.svg">\n',
    '  <link rel="stylesheet" href="./app.css">\n',
):
    html = html.replace(tag, "")

html = html.replace(
    "</head>",
    "<style>\n" + css + "\n</style>\n</head>",
    1,
)

for filename in ("engine.js", "core.js", "views.js", "app.js"):
    source = (ROOT / filename).read_text(encoding="utf-8")
    external = f'<script src="./{filename}" defer></script>'
    inline = "<script>\n" + source + "\n</script>"
    if external not in html:
        raise RuntimeError(f"Beklenen script etiketi bulunamadı: {external}")
    html = html.replace(external, inline, 1)

html = html.replace(
    "Bu uygulama JavaScript gerektirir. iPhone'da yerel dosya önizlemesi yerine GitHub Pages adresini Safari ile açın.",
    "Bu uygulama JavaScript gerektirir. JavaScript çalıştırabilen güncel bir tarayıcıyla açın.",
)

banner = "<!-- Bu dosya tools/build-standalone.py ile modüler runtime kaynaklarından otomatik üretilir. -->\n"
html = html.replace("<!doctype html>\n", "<!doctype html>\n" + banner, 1)

OUTPUT.write_text(html, encoding="utf-8")
print(f"Üretildi: {OUTPUT.name} ({OUTPUT.stat().st_size} byte)")
