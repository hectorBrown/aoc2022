PATH = "8/data.txt"


trees = [[int(y) for y in x[:-1]] for x in open(PATH, "r").readlines()]

masks = []
for i in range(max([tree for line in trees for tree in line]) + 1):
    masks.append(([[1 if tree >= i else 0 for tree in line] for line in trees]))

count = 0
for i, line in enumerate(trees):
    for j, tree in enumerate(line):
        mask = masks[tree]
        # horiz mask
        horiz = sum([2**k if val else 0 for k, val in enumerate(mask[i])])
        # vert mask
        vert = sum([2 ** k if mask[k][j] else 0 for k in range(len(mask))])
        vis = not (
            sum([2**k for k in range(j)]) & horiz > 0
            and sum([2**k for k in range(j + 1, len(line))]) & horiz > 0
        ) or not (
            sum([2**k for k in range(i)]) & vert > 0
            and sum([2**k for k in range(i + 1, len(trees))]) & vert > 0
        )
        if vis:
            count += 1

print(count)
