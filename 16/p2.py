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


def get_max_flow(pos, time, arrival, closed, pbar):
    character = None
    if arrival[0] == 0:
        character = 0
    else:
        character = 1
    options = []
    for c in closed:
        larger_in_route = [
            x not in chain.from_iterable(pos[character].routes[c.id])
            for x in filter(lambda z: z != c and z.flow > c.flow, closed)
        ]
        if all(larger_in_route) or len(larger_in_route) == 0:
            options.append(c)

    sub_paths = []
    if all([a == 0 for a in arrival]) and len(options) > 2:
        if character == 0:
            options = options[: int(len(options) / 2) + 1]
        else:
            options = options[int(len(options) / 2) - 1 :]
    for opt in options:
        new_arriv = [
            arrival[i] if i != character else len(pos[character].routes[opt.id][0]) + 2
            for i in range(2)
        ]
        new_pos = [pos[i] if i != character else opt for i in range(2)]
        if time > min(new_arriv):
            arriv_in = [new_arriv[i] - min(new_arriv) for i in range(2)]
            sub_paths.append(
                get_max_flow(
                    new_pos,
                    time=time - min(new_arriv),
                    arrival=arriv_in,
                    closed=list(filter(lambda x: x != opt, closed)),
                    pbar=pbar,
                )
            )
    if len(sub_paths) == 0:
        pbar.update(1)
        out = pos[character].flow * time
        if time > arrival[(character + 1) % 2]:
            out += pos[(character + 1) % 2].flow * (time - arrival[(character + 1) % 2])
        return out
    return max(sub_paths) + pos[character].flow * (time)


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

max_flow = get_max_flow(
    pos=[nodes["AA"], nodes["AA"]],
    time=26,
    arrival=[0, 0],
    closed=list(filter(lambda x: x.flow > 0, [nodes[n] for n in nodes])),
    pbar=pbar,
)

pbar.close()
print(max_flow)
