# UMBRI Manager

Tour planner for UMBRI, a melodic post-metal band from Rustavi, Georgia.

- **Live site:** https://bmenteshashvili.github.io/umbri-manager/
- Map of European venues that book metal, 3-night route options with drive times, flights from Tbilisi/Kutaisi, Fri–Sun weekends in 2027, and the log of booking emails sent.
- Data comes from the "UMBRI Outreach" Google Sheet (Venues, Promoters, Sent tabs).

## Update
Edit `src/data.js` (venues, sent log, routes) or `src/template.html` (page), then:

```
python3 build.py "Updated <date>"
```
and push to `main`. GitHub Pages serves `index.html` from the root.
