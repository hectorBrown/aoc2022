PATH = "9/data.txt"

commands = [
    [int(y) if i == 1 else y for i, y in enumerate(x[:-1].split(" "))]
    for x in open(PATH, "r").readlines()
]

dirmap = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

head = [0, 0]
tail = [0, 0]

visited = {0: {0: True}}

for command in commands:
    dir = dirmap[command[0]]
    for step in range(command[1]):
        head = [head[i] + dir[i] for i in range(2)]
        diff = [head[i] - tail[i] for i in range(2)]
        absdiff = [abs(x) for x in diff]
        if 2 in absdiff:
            tail = [tail[i] + dir[i] for i in range(2)]
            if 1 in absdiff:
                tail[absdiff.index(1)] += diff[absdiff.index(1)]
        if tail[0] not in visited:
            visited[tail[0]] = {}
        visited[tail[0]][tail[1]] = True


print(sum([len(visited[x]) for x in visited]))
