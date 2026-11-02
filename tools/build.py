"""Build index.html from src/editor.src.html by embedding the fonts in fonts/.

    python3 tools/build.py

The page has no other dependencies. It works offline as a single file.
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = {
    "VAZIR400": "Vazirmatn-Regular.woff2",
    "VAZIR500": "Vazirmatn-Medium.woff2",
    "VAZIR700": "Vazirmatn-Bold.woff2",
    "LALEZAR_AR": "lalezar-arabic-400-normal.woff2",
    "LALEZAR_LAT": "lalezar-latin-400-normal.woff2",
    "BARLOW600": "barlow-condensed-latin-600-normal.woff2",
    "BARLOW700": "barlow-condensed-latin-700-normal.woff2",
}

html = (ROOT / "src/editor.src.html").read_text(encoding="utf-8")
for key, name in FONTS.items():
    data = base64.b64encode((ROOT / "fonts" / name).read_bytes()).decode()
    html = html.replace("{{%s}}" % key, data)
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("wrote index.html")
