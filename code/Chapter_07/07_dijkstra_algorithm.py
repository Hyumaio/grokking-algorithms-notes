GRAPH = {
    'start': {'A': 6, 'B': 2},
    'A': {'end': 1},
    'B': {'A': 3, 'end': 5},
    'end': {}
}

INFINITY = float('inf')
COSTS = {
    'A': 6,
    'B': 2,
    'end': INFINITY
}

PARENTS = {
    'A': 'start',
    'B': 'start',
    'end': None
}

IS_PROCESSED = []


def get_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        # loop to get a lowest cost code which hasn't been processed
        if costs[node] < lowest_cost and node not in IS_PROCESSED:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == '__main__':
    node = get_lowest_cost_node(COSTS)
    while node is not None:
        to_node_lowest_cost = COSTS[node]
        node_neighbors_map = GRAPH[node]
        for neighbor in node_neighbors_map.keys():
            node_to_neighbor_cost = node_neighbors_map[neighbor]
            new_cost = to_node_lowest_cost + node_to_neighbor_cost
            if new_cost < COSTS[neighbor]:
                COSTS[neighbor] = new_cost
                PARENTS[neighbor] = node
        IS_PROCESSED.append(node)
        node = get_lowest_cost_node(COSTS)
    for i in COSTS:
        print("From start to {}'s lowest cost is {}.".format(i, COSTS[i]))
