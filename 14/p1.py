# this one is slow but will eventually work
PATH = "14/data.txt"

import os
import sys
from itertools import chain

from tqdm import tqdm

sys.path.append(os.path.abspath("."))
from util import Vect

lines = [
    [[int(z) for z in y.split(",")] for y in x[:-1].split(" -> ")]
    for x in open(PATH, "r").readlines()
]

void = max(list(chain.from_iterable([[y[1] for y in x] for x in lines])))
rock = []
for line in lines:
    for pts in zip(line, line[1:]):
        if pts[0][0] == pts[1][0]:
            for i in range(*[y + i for i, y in enumerate(sorted([x[1] for x in pts]))]):
                rock.append(Vect(pts[0][0], i))
        else:
            for i in range(*[y + i for i, y in enumerate(sorted([x[0] for x in pts]))]):
                rock.append(Vect(i, pts[0][1]))
    rock.append(Vect(*line[-1]))
rock = list(set(rock))

stable = False
count = 0
pbar = tqdm()
while not stable:
    count += 1
    sand = Vect(500, 0)
    moving = True
    while moving:
        moving = False
        if sand.y >= void:
            count -= 1
            moving = False
            stable = True
        elif Vect(sand.x, sand.y + 1) not in rock:
            sand.move(0, 1)
            moving = True
        elif Vect(sand.x - 1, sand.y + 1) not in rock:
            sand.move(-1, 1)
            moving = True
        elif Vect(sand.x + 1, sand.y + 1) not in rock:
            sand.move(1, 1)
            moving = True
    rock.append(sand)
    pbar.update(1)
pbar.close()

print(count)
