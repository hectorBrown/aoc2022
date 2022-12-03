PATH = "3/data.txt"
rucksacks = [
    (x[:-1][: int(len(x) / 2)], x[:-1][int(len(x) / 2) :])
    for x in open(PATH, "r").readlines()
]


def get_common(rucksack):
    for item in rucksack[0]:
        if item in rucksack[1]:
            return item


def get_priority(item):
    ch = ord(item)
    if ch >= 97:
        return ch - 97 + 1
    else:
        return ch - 65 + 27


priority_sum = 0
for rucksack in rucksacks:
    item = get_common(rucksack)
    priority_sum += get_priority(item)
print(priority_sum)
