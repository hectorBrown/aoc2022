PATH = "4/data.txt"

pairs = [
    [
        sum([2**i for i in range(*[int(z) + i for i, z in enumerate(y.split("-"))])])
        for y in x[:-1].split(",")
    ]
    for x in open(PATH, "r").readlines()
]

print(sum([pair[0] | pair[1] in pair for pair in pairs]))
