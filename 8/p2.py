PATH = "8/data.txt"

trees = [[int(y) for y in x[:-1]] for x in open(PATH, "r").readlines()]

masks = []
for i in range(max([tree for line in trees for tree in line]) + 1):
    masks.append(([[1 if tree >= i else 0 for tree in line] for line in trees]))

scores = []
for i, line in enumerate(trees):
    for j, tree in enumerate(line):
        score = 1
        mask = masks[tree]

        dirs = []
        dirs.append("".join([str(mask[k][j]) for k in range(i)][::-1]))
        dirs.append("".join([str(mask[k][j]) for k in range(i + 1, len(trees))]))
        dirs.append("".join([str(mask[i][k]) for k in range(j)][::-1]))
        dirs.append("".join([str(mask[i][k]) for k in range(j + 1, len(line))]))

        for dir in dirs:
            count = 0
            scan = True
            while scan:
                if count < len(dir):
                    if dir[count] == "0":
                        count += 1
                    else:
                        count += 1
                        scan = False
                else:
                    scan = False
            score *= count

        scores.append(score)

print(max(scores))
