PATH = "2/data.txt"

rounds = [[ord(y) for y in x[:-1].split(" ")] for x in open(PATH, "r").readlines()]
rounds = [[x - 64, y - 23 - 64] for x, y in rounds]

score = 0
for round in rounds:
    if (round[1] - round[0]) % 3 == 1:
        score += 6
    elif round[0] == round[1]:
        score += 3
    else:
        score += 0
    score += round[1]

print(score)
