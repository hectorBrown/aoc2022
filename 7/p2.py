PATH = "7/data.txt"


class Dir:
    def __init__(self, parent):
        self.children = {}
        self.parent = parent

    def add_child(self, child, id):
        self.children[id] = child

    def size(self):
        if len(self.children) == 0:
            return 0
        else:
            return sum([self.children[x].size() for x in self.children])


class File:
    def __init__(self, size):
        self._size = size

    def size(self):
        return self._size


commands = [x[1:-1] for x in open(PATH, "r").read().split("$")[1:]]

tot_space = 70000000
nec_space = 30000000

root = Dir(None)
pointer = None

dirs = [root]

for command in commands:
    if command[:2] == "cd":
        target = command.split(" ")[1]
        if target == "/":
            pointer = root
        elif target == "..":
            pointer = pointer.parent
        else:
            pointer = pointer.children[target]
    else:
        output = command.split("\n")[1:]
        for child in output:
            if child[0] == "d":
                dirs.append(Dir(pointer))
                pointer.add_child(dirs[-1], child.split(" ")[1])
            else:
                pointer.add_child(File(int(child.split(" ")[0])), child.split(" ")[1])

used_space = root.size()
free_space = tot_space - used_space
req_space = nec_space - free_space

print(sorted(filter(lambda x: x > req_space, [x.size() for x in dirs]))[0])
