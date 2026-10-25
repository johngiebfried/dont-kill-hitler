#!/usr/bin/env python3
"""Build platformer/index.html from platformer/index.src.html by inlining the land-mask map data
(tools/mapdata.json: a coarse world grid and a 0.5-degree Europe grid sampled from the GLOBE land mask
via the global-land-mask package). The output stays a single self-contained file that runs from file://."""
import json, pathlib, sys
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "platformer" / "index.src.html").read_text(encoding="utf-8")
data = json.loads((root / "tools" / "mapdata.json").read_text(encoding="utf-8"))
if src.count("__MAPDATA__") != 1: sys.exit("placeholder __MAPDATA__ not found exactly once")
(root / "platformer" / "index.html").write_text(src.replace("__MAPDATA__", json.dumps(data, separators=(",", ":"))), encoding="utf-8")
print("wrote platformer/index.html")
