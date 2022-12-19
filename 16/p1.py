import re
from itertools import chain

PATH = "16/ex.txt"


class Node:
    def __init__(self, id, flow):
        self.id = id
        self.flow = flow
        self.linked = None
        self.routes = {}

    def __eq__(self, other):
        return self.id == other.id

    def __repr__(self):
        return "{{{}, flow {}: {}}}".format(
            self.id, self.flow, [l.id for l in self.linked]
        )

    def add_linked(self, linked):
        self.linked = linked


def get_routes(start, end):
    active = [[l] for l in start.linked]
    while end not in [x[-1] for x in active]:
        active = list(
            filter(
                lambda x: x[-1] not in chain.from_iterable([x[:-1] for x in active]),
                [x + [l] for x in active for l in x[-1].linked],
            )
        )
    return [x[:-1] for x in filter(lambda x: x[-1] == end, active)]


def get_paths(pos, time, closed):
    options = []
    for c in closed:
        larger_in_route = [
            x not in chain.from_iterable(pos.routes[c.id])
            for x in filter(lambda z: z != c and z.flow > c.flow, closed)
        ]
        if all(larger_in_route) or len(larger_in_route) == 0:
            options.append(c)


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

for id in nodes:
    nodes[id].routes = {
        x: get_routes(nodes[id], nodes[x]) for x in filter(lambda x: x != id, nodes)
    }
get_paths(
    nodes["AA"],
    time=0,
    closed=list(filter(lambda x: x.flow > 0, [nodes[n] for n in nodes])),
)
