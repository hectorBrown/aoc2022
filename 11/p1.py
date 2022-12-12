import re

PATH = "11/data.txt"


class Monkey:
    def __init__(self, raw_monkey):
        self.items = [int(x) for x in raw_monkey[1].split(":")[1].split(",")]
        raw_op = raw_monkey[2].split("=")[1][1:]
        args = raw_op.split("*" if "*" in raw_op else "+")
        for i, arg in enumerate(args):
            args[i] = (lambda x: x) if "old" in arg else (lambda x: int(arg))
        self._operation = (
            (lambda x: args.copy()[0](x) * args.copy()[1](x))
            if "*" in raw_op
            else (lambda x: args.copy()[0](x) + args.copy()[1](x))
        )
        self._test = lambda x: x % int(re.findall(r"\d+$", raw_monkey[3])[0]) == 0
        self._target = {}
        self._target[True] = int(re.findall(r"\d+$", raw_monkey[4])[0])
        self._target[False] = int(re.findall(r"\d+$", raw_monkey[5])[0])

    def __repr__(self):
        return str(self.items)

    def catch(self, item):
        self.items.append(item)

    def inspect_all(self, monkeys):
        inspections = 0
        while len(self.items) > 0:
            inspections += 1
            self.inspect(monkeys)
        return inspections

    def inspect(self, monkeys):
        item = self.items.pop(0)
        item = self._operation(item)
        item = int(item / 3)
        monkeys[self._target[self._test(item)]].catch(item)


raw = [x.split("\n") for x in open(PATH, "r").read().split("\n\n")]

monkeys = []

for raw_monkey in raw:
    monkeys.append(Monkey(raw_monkey))

inspections = [0] * len(monkeys)
for i in range(20):
    for i, monkey in enumerate(monkeys):
        inspections[i] += monkey.inspect_all(monkeys)

inspections = sorted(inspections)[::-1]
print(inspections[0] * inspections[1])
