import re
from itertools import chain

from tqdm import tqdm

PATH = "16/data.txt"


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


def get_max_flow(pos, time, closed, pbar):
    options = []
    for c in closed:
        larger_in_route = [
            x not in chain.from_iterable(pos.routes[c.id])
            for x in filter(lambda z: z != c and z.flow > c.flow, closed)
        ]
        if all(larger_in_route) or len(larger_in_route) == 0:
            options.append(c)

    sub_paths = []
    for opt in options:
        if time > len(pos.routes[opt.id][0]) + 2:
            sub_paths.append(
                get_max_flow(
                    opt,
                    time=time
                    - len(pos.routes[opt.id][0])
                    - (1 if pos.id == "AA" else 2),
                    closed=list(filter(lambda x: x != opt, closed)),
                    pbar=pbar,
                )
            )
    if len(sub_paths) == 0:
        pbar.update(1)
        return (time - 1) * pos.flow
    return max(sub_paths) + (time - 1) * pos.flow


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

pbar = tqdm()
for id in nodes:
    nodes[id].routes = {
        x: get_routes(nodes[id], nodes[x]) for x in filter(lambda x: x != id, nodes)
    }
    pbar.update(1)

ids = list(filter(lambda x: nodes[x].flow != 0, nodes))
time = 30
moving = True
flow = 0
pos = nodes["AA"]
compare(nodes["AA"], nodes["DD"], nodes["JJ"])
while moving:
    print(ids)
    comparisons = [
        [None if idi == idj else compare(pos, nodes[idi], nodes[idj]) for idi in ids]
        for idj in ids
    ]
    print("\n".join([str(x) for x in comparisons]))
    moving = False
