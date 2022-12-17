import re

PATH = "16/ex.txt"


class Node:
    def __init__(self, id, flow):
        self.id = id
        self.flow = flow
        self.linked = None

    def __repr__(self):
        return "({}, flow {}: {})".format(
            self.id, self.flow, [l.id for l in self.linked]
        )

    def add_linked(self, linked):
        self.linked = linked


nodes_linked = {
    node[0]: (Node(node[0], int(node[1])), node[2].split(", "))
    for node in [
        re.match(
            r"^Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? (([A-Z]{2}(, )?)+)$",
            x[:-1],
        ).groups()[:-2]
        for x in open(PATH, "r").readlines()
    ]
}
nodes = {}

for node in nodes_linked:
    nodes[node] = nodes_linked[node][0]
    nodes[node].add_linked([nodes_linked[i][0] for i in nodes_linked[node][1]])

print(nodes)
