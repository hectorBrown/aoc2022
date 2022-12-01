PATH = "1/data.txt"
print(
    max(
        [
            sum([int(y) for y in x.split("\n")])
            for x in open(PATH, "r").read()[:-1].split("\n\n")
        ]
    )
)
