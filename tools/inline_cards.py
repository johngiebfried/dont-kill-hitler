#!/usr/bin/env python3
"""Inline card-game/data/cards.json and the table-mat map grid into card-game/index.html
(so the walkthrough runs from file://).

Card text is approved copy: edit it only in data/cards.json, then run:
    python3 tools/inline_cards.py
The map grid (tools/ce_mapdata.json, Central Europe land mask at 0.1 degrees) comes from tools/make_mapdata.py.
"""
import json, pathlib, sys

root = pathlib.Path(__file__).resolve().parent.parent
src = root / "card-game" / "index.src.html"
data = root / "card-game" / "data" / "cards.json"
mapdata = root / "tools" / "ce_mapdata.json"
out = root / "card-game" / "index.html"

raw = data.read_text(encoding="utf-8")
json.loads(raw)  # fail loudly on invalid JSON
if "</" in raw:
    sys.exit("cards.json contains '</', which would break the inline <script>; escape it first.")
grid = mapdata.read_text(encoding="utf-8").strip()
json.loads(grid)
html = src.read_text(encoding="utf-8")
for ph in ("__CARDS_JSON__", "__MAP_JSON__"):
    if html.count(ph) != 1:
        sys.exit(f"placeholder {ph} not found exactly once in index.src.html")
out.write_text(html.replace("__CARDS_JSON__", raw).replace("__MAP_JSON__", grid), encoding="utf-8")
print(f"wrote {out.relative_to(root)} ({len(raw)} bytes of card data, {len(grid)} bytes of map grid)")
