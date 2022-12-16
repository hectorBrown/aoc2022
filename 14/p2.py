# this one is slow but will eventually work
PATH = "14/data.txt"

import os
import sys
from itertools import chain

sys.path.append(os.path.abspath("."))
from util import Vect

lines = [
    [[int(z) for z in y.split(",")] for y in x[:-1].split(" -> ")]
    for x in open(PATH, "r").readlines()
]

floor = max(list(chain.from_iterable([[y[1] for y in x] for x in lines]))) + 2
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

nodes = [Vect(500, 0)]
count = 1
for i in range(floor - 1):
    nodes = list(
        set(
            filter(
                lambda x: x not in rock,
                [Vect(node.x + i, node.y + 1) for i in range(-1, 2) for node in nodes],
            )
        )
    )
    count += len(nodes)

print(count)
