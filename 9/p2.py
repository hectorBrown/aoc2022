PATH = "9/data.txt"

commands = [
    [int(y) if i == 1 else y for i, y in enumerate(x[:-1].split(" "))]
    for x in open(PATH, "r").readlines()
]

dirmap = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

head = [0, 0]
rope = [[0, 0] for i in range(9)]

visited = {0: {0: True}}

for command in commands:
    dir = dirmap[command[0]]
    for step in range(command[1]):
        head = [head[i] + dir[i] for i in range(2)]
        for j in range(len(rope)):
            loc_head = head if j == 0 else rope[j - 1]
            diff = [loc_head[i] - rope[j][i] for i in range(2)]
            absdiff = [abs(x) for x in diff]
            if 2 in absdiff:
                rope[j] = [
                    rope[j][i]
                    + [0 if diff[k] == 0 else diff[k] / abs(diff[k]) for k in range(2)][
                        i
                    ]
                    for i in range(2)
                ]
        if rope[-1][0] not in visited:
            visited[rope[-1][0]] = {}
        visited[rope[-1][0]][rope[-1][1]] = True


print(sum([len(visited[x]) for x in visited]))
