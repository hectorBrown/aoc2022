PATH = "14/data.txt"

from itertools import chain


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (
            2 ** abs(self.x)
            * 3 ** (abs(self.y))
            * 5 ** int(self.x / abs(self.x) + 1)
            * 7 ** int(self.y / abs(self.y) + 1)
        )

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def move(self, x, y):
        self.x += x
        self.y += y


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
                rock.append(Pos(pts[0][0], i))
        else:
            for i in range(*[y + i for i, y in enumerate(sorted([x[0] for x in pts]))]):
                rock.append(Pos(i, pts[0][1]))
    rock.append(Pos(*line[-1]))
rock = list(set(rock))

stable = False
count = 0
while not stable:
    count += 1
    sand = Pos(500, 0)
    moving = True
    while moving:
        moving = False
        if sand.y >= void:
            count -= 1
            moving = False
            stable = True
        elif Pos(sand.x, sand.y + 1) not in rock:
            sand.move(0, 1)
            moving = True
        elif Pos(sand.x - 1, sand.y + 1) not in rock:
            sand.move(-1, 1)
            moving = True
        elif Pos(sand.x + 1, sand.y + 1) not in rock:
            sand.move(1, 1)
            moving = True
    rock.append(sand)

print(count)
