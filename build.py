#!/usr/bin/env python3
"""Build index.html from src/. Usage: python3 build.py "Updated 25 Nov 2026, 21:20 (Tbilisi)" """
import sys, pathlib
root = pathlib.Path(__file__).parent
stamp = sys.argv[1] if len(sys.argv) > 1 else "Saved copy"
t = (root/"src/template.html").read_text()
t = t.replace("live='Saved copy (connect to see live data)'", "live=" + repr(stamp))
t = t.replace("live='Saved copy · live data not available in this view'", "live=" + repr(stamp))
html = t.replace("__GEO__", (root/"src/geo.json").read_text()).replace("__DATA__", (root/"src/data.js").read_text())
(root/"index.html").write_text(html)
print("built index.html", len(html))
