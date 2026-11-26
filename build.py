#!/usr/bin/env python3
"""Build index.html from src/. Usage: python3 build.py "Updated 25 Nov 2026, 21:20 (Tbilisi)" """
import sys, pathlib
root = pathlib.Path(__file__).parent
args=[a for a in sys.argv[1:] if not a.startswith("--")]
stamp = args[0] if args else "Saved copy"
leaf = "--claude" not in sys.argv
t = (root/"src/template.html").read_text()
t = t.replace("live='Saved copy (connect to see live data)'", "live=" + repr(stamp))
t = t.replace("live='Saved copy · live data not available in this view'", "live=" + repr(stamp))
t = t.replace("__BUILT__", stamp.replace("'",""))
html = t.replace("__GEO__", (root/"src/geo.json").read_text()).replace("__DATA__", (root/"src/data.js").read_text())
if leaf:
    html = html.replace("</title>", '</title>\n<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">\n<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>', 1)
out = root/("index.html" if leaf else "claude.html")
out.write_text(html)
print("built", out.name, len(html))
