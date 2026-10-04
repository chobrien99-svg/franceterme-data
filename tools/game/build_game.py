"""Rebuild game/index.html from FranceTerme.xml.

Run from the repo root:   python3 tools/game/build_game.py
1. Download the latest FranceTerme.xml into the repo root (see README).
2. Run this script. It re-reads the official definitions/years for every
   curated term, warns about any term that changed or disappeared, and
   writes game/index.html.
To add or remove words, edit the lists in tools/game/gamedata.json.
"""
import json, re, xml.etree.ElementTree as ET, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
HERE = pathlib.Path(__file__).resolve().parent
root = ET.parse(ROOT / "FranceTerme.xml").getroot()
by_en = {}
for a in root.findall("Article"):
    if a.get("annule") == "1" or a.get("publie") != "1": continue
    t = a.find("Terme[@statut='privilegie']")
    if t is None: continue
    for e in a.findall("Equivalent[@langue='en']/Equi_prop"):
        if e.text and e.text.strip():
            by_en.setdefault(e.text.strip().lower(), []).append(a)
def refresh(term):
    arts = by_en.get(term["en"].lower(), [])
    def fr_of(a):
        fr = a.find("Terme[@statut='privilegie']").get("Terme")
        m = re.match(r"^(.*) \((à|en|de)\)$", fr)
        return m.group(2) + " " + m.group(1) if m else fr
    match = [a for a in arts if fr_of(a) == term["fr"]]
    if not match:
        print(f"  ! check: '{term['en']}' -> '{term['fr']}' no longer matches the database:", [fr_of(a) for a in arts] or "missing")
        return term
    a = match[0]
    d = re.sub(r"\s+", " ", (a.findtext("Definition") or "")).strip()
    d = re.split(r"(?<=[.;])\s", d)[0]
    if len(d) > 150: d = d[:147].rsplit(" ", 1)[0] + "…"
    term["d"] = d
    date = a.findtext("DatePub") or ""
    term["year"] = date[-4:]
    return term
data = json.loads((HERE / "gamedata.json").read_text(encoding="utf-8"))
data["terms"] = [refresh(t) for t in data["terms"]]
data["bosses"] = [refresh(t) for t in data["bosses"]]
(HERE / "gamedata.json").write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
html = (HERE / "template.html").read_text(encoding="utf-8").replace("/*DATA*/", json.dumps(data, ensure_ascii=False))
(ROOT / "game").mkdir(exist_ok=True)
(ROOT / "game" / "index.html").write_text(html, encoding="utf-8")
print(f"Built game/index.html with {len(data['terms'])} terms and {len(data['bosses'])} bosses.")
