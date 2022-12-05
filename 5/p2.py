PATH = "5/data.txt"

# just parsing
lines = open(PATH, "r").read().split("\n\n")

raw_stacks = lines[0].split("\n")
raw_instructions = lines[1].split("\n")[:-1]

stacks = []
for i in range(len(raw_stacks[-1].split("  "))):
    stacks.append([])
    for level in raw_stacks[-2::-1]:
        item = None
        if len(level) > 4 * i + 1:
            item = level[4 * i + 1]
        else:
            item = " "
        if not item == " ":
            stacks[-1].append(item)

instructions = []
for instruction in raw_instructions:
    num, pos = instruction.split(" from ")
    num = int(num.split(" ")[1])
    pos = [int(x) - 1 for x in pos.split(" to ")]
    instructions.append((num, *pos))

# actual code
for ins in instructions:
    stacks[ins[2]] += stacks[ins[1]][-ins[0] :]
    stacks[ins[1]] = stacks[ins[1]][: -ins[0]]

output = ""
for stack in stacks:
    output += stack[-1]
print(output)
