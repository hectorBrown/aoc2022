PATH = "6/data.txt"


def sop_marker(buffer):
    for ch in range(3, len(buffer)):
        if len(set(buffer[ch - 4 : ch])) == 4:
            return ch


buffer = open(PATH, "r").read()[:-1]

print(sop_marker(buffer))
