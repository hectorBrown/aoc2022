import re
from itertools import chain

PATH = "13/data.txt"


class Packet:
    def __init__(self, raw, divider=False):
        self.divider = divider
        raw = raw[1:-1]
        children = []
        self.children = []
        level = 0
        prev = 0
        for i, scan in enumerate(raw):
            if scan == "[":
                level += 1
            elif scan == "]":
                level -= 1
            elif level == 0 and scan == ",":
                children.append(raw[prev:i])
                prev = i + 1
            if i == len(raw) - 1:
                children.append(raw[prev:])
        for child in children:
            if re.match(r"^\d+$", child) is None:
                self.children.append(Packet(child))
            else:
                self.children.append(int(child))

    def __repr__(self):
        res = "["
        for i, child in enumerate(self.children):
            res += str(child) + (", " if i != len(self.children) - 1 else "")
        res += "]"
        return res

    def compare(self, other):
        # assuming self is the left packet
        default = (
            None
            if len(self.children) == len(other.children)
            else len(self.children) < len(other.children)
        )
        for ch_s, ch_o in zip(self.children, other.children):
            res = None
            if type(ch_s) is Packet or type(ch_o) is Packet:
                res = (ch_s if type(ch_s) is Packet else Packet(f"[{ch_s}]")).compare(
                    ch_o if type(ch_o) is Packet else Packet(f"[{ch_o}]")
                )
            else:
                res = None if ch_s == ch_o else ch_s < ch_o
            if not res is None:
                return res
        return default


packets = [
    Packet(packet)
    for packet in list(
        chain.from_iterable(
            [x.split("\n") for x in open(PATH, "r").read().split("\n\n")]
        )
    )[:-1]
]
packets += [Packet(packet, divider=True) for packet in ["[[2]]", "[[6]]"]]

changes = True
while changes:
    changes = False
    for i in range(len(packets) - 1):
        if not packets[i].compare(packets[i + 1]):
            packets[i], packets[i + 1] = packets[i + 1], packets[i]
            changes = True

key = 1
for i, packet in enumerate(packets):
    if packet.divider:
        key *= i + 1
print(key)
