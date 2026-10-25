from global_land_mask import globe
import numpy as np, json
# Land masks as hex-encoded rows of bits (1 = land).
# mapdata.json: world (1.5 deg) and Europe (0.5 deg) grids for the platformer's conquest maps.
# ce_mapdata.json: Central Europe at 0.1 deg for the card game's table mats (one sample per cell center).
def grid(lon0, lon1, lat0, lat1, step):
    lons = np.arange(lon0, lon1, step); lats = np.arange(lat1, lat0, -step)
    rows = []
    for la in lats:
        bits = []
        for lo in lons:
            pts = [(la - step*a, lo + step*b) for a in (0.25, 0.75) for b in (0.25, 0.75)]
            n = sum(globe.is_land(p[0], p[1]) for p in pts)
            bits.append(1 if n >= 2 else 0)
        s = ''.join(str(b) for b in bits)
        s += '0' * ((-len(s)) % 4)
        rows.append(''.join('%x' % int(s[i:i+4], 2) for i in range(0, len(s), 4)))
    return {'lon0': lon0, 'lat1': lat1, 'step': step, 'cols': len(lons), 'rows': len(lats), 'data': rows}
def fine(lon0, lon1, lat0, lat1, step):
    lons = np.arange(lon0, lon1, step) + step/2
    lats = np.arange(lat1, lat0, -step) - step/2
    LO, LA = np.meshgrid(lons, lats)
    m = globe.is_land(LA, LO)
    rows = []
    for r in m:
        s = ''.join('1' if b else '0' for b in r); s += '0' * ((-len(s)) % 4)
        rows.append(''.join('%x' % int(s[i:i+4], 2) for i in range(0, len(s), 4)))
    return {'lon0': lon0, 'lat1': lat1, 'step': step, 'cols': len(lons), 'rows': len(lats), 'data': rows}
out = {'world': grid(-180, 180, -58, 80, 1.5), 'europe': grid(-14, 66, 24, 72, 0.5)}
json.dump(out, open('mapdata.json', 'w'), separators=(',', ':'))
json.dump(fine(-6, 26, 40, 58, 0.1), open('ce_mapdata.json', 'w'), separators=(',', ':'))
print(out['world']['cols'], out['world']['rows'], out['europe']['cols'], out['europe']['rows'])
