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

floor = max(list(chain.from_iterable([[y[1] for y in x] for x in lines]))) + 2
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

nodes = [Pos(500, 0)]
count = 1
for i in range(floor - 1):
    nodes = list(
        set(
            filter(
                lambda x: x not in rock,
                [Pos(node.x + i, node.y + 1) for i in range(-1, 2) for node in nodes],
            )
        )
    )
    count += len(nodes)

print(count)
