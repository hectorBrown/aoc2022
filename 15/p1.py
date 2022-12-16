import os
import re
import sys

from tqdm import tqdm

sys.path.append(os.path.abspath("."))
from util import Vect

PATH = "15/data.txt"
y = 10 if "ex" in PATH else 2000000


sensors = [
    [Vect(*[int(z) for z in re.findall(r"[xy]=(-?\d+)", y)]) for y in x.split(":")]
    for x in open(PATH, "r").readlines()
]

no_beacon = []
pbar = tqdm(total=len(sensors))
for sensor in sensors:
    dist = sensor[1] - sensor[0]
    rad = abs(dist.x) + abs(dist.y)
    width = rad - abs(y - sensor[0].y)
    width = 0 if width < 0 else width
    no_beacon += [sensor[0].x + i for i in range(-width, width + 1)]
    no_beacon = list(set(no_beacon))
    if sensor[1].y == y:
        no_beacon.pop(no_beacon.index(sensor[1].x))
    pbar.update(1)

pbar.close()
print(len(no_beacon))
