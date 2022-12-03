import numpy as np

PATH = "3/data.txt"

groups = (
    np.array([x[:-1] for x in open(PATH, "r").readlines()]).reshape((-1, 3)).tolist()
)


def get_common(group):
    for item in group[0]:
        if item in group[1] and item in group[2]:
            return item


def get_priority(item):
    ch = ord(item)
    if ch >= 97:
        return ch - 97 + 1
    else:
        return ch - 65 + 27


priority_sum = 0
for group in groups:
    badge = get_common(group)
    priority_sum += get_priority(badge)

print(priority_sum)
