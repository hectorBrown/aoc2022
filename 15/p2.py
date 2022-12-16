# takes a while to run, it will work
import os
import re
import sys

from tqdm import tqdm

sys.path.append(os.path.abspath("."))
from util import Vect

PATH = "15/data.txt"
max = 20 if "ex" in PATH else 4000000


def get_move(sensors, pos):
    for sensor in sensors:
        rad_vect = sensor[1] - sensor[0]
        rad = abs(rad_vect.x) + abs(rad_vect.y)
        width = rad - abs(pos.y - sensor[0].y)
        width = 0 if width < 0 else width
        dist = pos - sensor[0]
        dist = abs(dist.x) + abs(dist.y)

        if dist <= rad:
            return (sensor[0].x - pos.x) + width + 1


sensors = [
    [Vect(*[int(z) for z in re.findall(r"[xy]=(-?\d+)", y)]) for y in x.split(":")]
    for x in open(PATH, "r").readlines()
]

pos = Vect(0, 0)
move = 0
pbar = tqdm(total=max)
while not move is None:
    move = get_move(sensors, pos)
    if not move is None:
        pos.move(move, 0)
        if pos.x > max:
            pos = Vect(0, pos.y + 1)
            pbar.update(1)
pbar.close()
print(pos.x * 4000000 + pos.y)
