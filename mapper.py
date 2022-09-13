#!/usr/bin/env python3
import sys


class NodeStructure:
    def __init__(self, node_id, adj_list, dist):
        self.node_id = node_id
        self.adj_list = adj_list
        self.dist = dist


# breadth first search mapper

def get_distances(filename):
    distances = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            values = line.split(' ')  # split distance.txt values into node id + distance
            distances[values[0]] = values[1]

    return distances


def create_nodes(distances):
    nodes = []
    for line in sys.stdin:
        line = line.strip()
        adj_list = line.split(' ')
        node_id = adj_list[0]
        adj_list.pop(0)
        distance = distances[node_id]
        node_id = node_id.strip(':')

        nodes.append(NodeStructure(node_id, adj_list, distance))

    return nodes


def emit_nodes(nodes):
    for n in nodes:
        print(n.node_id, int(n.dist))
        for node in n.adj_list:
            if node != 'none':
                print(node, int(n.dist) + 1)



if __name__ == "__main__":
    distances = get_distances('distance.txt')
    nodes = create_nodes(distances)
    emit_nodes(nodes)
