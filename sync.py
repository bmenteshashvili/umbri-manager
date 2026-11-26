#!/usr/bin/env python3
"""Rewrite src/data.js VENUES and SENT0 from Google Sheet exports.
Usage: python3 sync.py venues.json sent.json   (each = get_values output {"values":[...]})"""
import json, re, sys, pathlib
root = pathlib.Path(__file__).parent
def load(p):
    d = json.load(open(p)); return d.get('values', d)
def num(x):
    try: return float(x)
    except Exception: return None
V = load(sys.argv[1]); H = [h.lower() for h in V[0]]
def g(r, n):
    i = next((i for i, h in enumerate(H) if h.startswith(n)), -1)
    return (str(r[i]) if 0 <= i < len(r) else '').lstrip("'")
ven = []
for r in V[1:]:
    if not r or not g(r, 'name'): continue
    a = g(r, 'address')
    ven.append(dict(id=g(r,'id'), name=g(r,'name'), country=g(r,'country'), city=g(r,'city'),
        address=re.sub(r'\s*\(pin approximate\)', '', a), lat=num(g(r,'lat')), lng=num(g(r,'lng')),
        approx='approximate' in a.lower(), cap=g(r,'capacity'), email=g(r,'booking email'), phone=g(r,'phone'),
        contact=g(r,'contact person'), web=g(r,'website'), social=g(r,'instagram'), photos=g(r,'photos'),
        fit=g(r,'metal fit'), conf=g(r,'contact confidence'), src=g(r,'sources'), status=g(r,'status')))
S = load(sys.argv[2]); sent = []
for r in S[1:]:
    r = list(r) + [''] * 12
    if not (r[2] or r[5]): continue
    sent.append(dict(date=r[0], id=r[1], name=r[2], city=r[3], country=r[4], email=r[5], link=r[7],
                     status=r[8], follow=r[9], reply=r[10], summary=r[11]))
p = root/'src/data.js'; s = p.read_text()
a = s.index('let VENUES=['); b = s.index('const SENT0='); c = s.index('\n', b)
s = s[:a] + 'let VENUES=[\n' + ',\n'.join(json.dumps(v, ensure_ascii=False) for v in ven) + '\n];\n' + \
    'const SENT0=' + json.dumps(sent, ensure_ascii=False) + ';' + s[c:]
p.write_text(s); print('venues', len(ven), 'sent', len(sent))
