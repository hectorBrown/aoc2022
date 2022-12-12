PATH = "10/data.txt"

instructions = [
    [int(y) if i == 1 else y for i, y in enumerate(x[:-1].split(" "))]
    for x in open(PATH, "r").readlines()
][::-1]

executing = True
curr = [None, 0]
registers = {"X": 1}
crt = 0
crt_out = ""
periods = {"noop": 1, "addx": 2}
cycle = 0

while executing:
    # before
    cycle += 1
    if curr[1] == 0:
        new = instructions.pop()
        curr = [new, periods[new[0]]]

    # during
    if abs(crt % 40 - registers["X"]) <= 1:
        crt_out += "#"
    else:
        crt_out += "."

    # after
    if curr[1] == 1:
        if curr[0][0] == "addx":
            registers["X"] += curr[0][1]

    curr[1] -= 1
    crt += 1
    if len(instructions) == 0:
        executing = False


crt_out = "\n".join([crt_out[40 * i : 40 * (i + 1)] for i in range(6)])
print(crt_out)
