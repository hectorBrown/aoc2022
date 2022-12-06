PATH = "6/data.txt"


def som_marker(buffer):
    for ch in range(13, len(buffer)):
        if len(set(buffer[ch - 14 : ch])) == 14:
            return ch


buffer = open(PATH, "r").read()[:-1]

print(som_marker(buffer))
