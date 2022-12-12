PATH = "12/data.txt"


class Loc:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __eq__(self, other):
        return self.i == other.i and self.j == other.j

    def __hash__(self):
        sign_i = 0 if self.i == 0 else int(self.i / abs(self.i))
        sign_j = 0 if self.j == 0 else int(self.j / abs(self.j))
        return (
            2 ** abs(self.i) * 3 ** abs(self.j) * 5 ** (sign_i + 1) * 7 ** (sign_j + 1)
        )

    def __repr__(self):
        return "[{}, {}]".format(self.i, self.j)

    def get_neig(self, map):
        neig = []
        for i_s in range(-1, 2):
            for j_s in range(-1, 2):
                if not (i_s == j_s) and not (i_s + j_s == 0):
                    y = self.i + i_s
                    x = self.j + j_s
                    if y in range(len(map)) and x in range(len(map[0])):
                        neig.append(Loc(y, x))
        return neig


map = [x[:-1] for x in open(PATH, "r").readlines()]

S, E = None, None

for i, line in enumerate(map):
    map[i] = [ord(x) - 97 for x in line]
    if -14 in map[i]:
        S = Loc(i, map[i].index(-14))
        map[i][map[i].index(-14)] = ord("a") - 97
    if -28 in map[i]:
        E = Loc(i, map[i].index(-28))
        map[i][map[i].index(-28)] = ord("z") - 97


distances = {E: 0}
active = [E]

while S not in distances:
    new_active = []
    for loc in active:
        neigs = loc.get_neig(map)
        for neig in neigs:
            if map[neig.i][neig.j] >= map[loc.i][loc.j] - 1 and not neig in distances:
                distances[neig] = distances[loc] + 1
                new_active.append(neig)
    active = new_active.copy()

print(distances[S])
