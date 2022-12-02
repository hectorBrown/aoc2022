PATH = "2/data.txt"

rounds = [[ord(y) for y in x[:-1].split(" ")] for x in open(PATH, "r").readlines()]
rounds = [[x - 65, y - 23 - 65 - 1] for x, y in rounds]

score = 0
for round in rounds:
    score += 3 * (round[1] + 1)
    score += (round[0] + round[1]) % 3 + 1

print(score)
