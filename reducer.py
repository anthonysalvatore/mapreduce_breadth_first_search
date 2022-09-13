#!/usr/bin/env python3
import sys


def retrieve_nodes():
    nodes = {}
    current_node = None

    for line in sys.stdin:
        line = line.strip()
        node_id, d = line.split(' ', 1)

        if current_node == node_id:
            node_data.append(int(d))
        else:
            if current_node:
                nodes[current_node] = node_data
            current_node = node_id
            node_data = []
            node_data.append(int(d))

    nodes[current_node] = node_data

    return nodes


def minimum_distance(nodes):
    for node_id, d in nodes.items():
        min_d = min(d)
        print(node_id + ':', min_d)


if __name__ == '__main__':
    nodes = retrieve_nodes()
    minimum_distance(nodes)
