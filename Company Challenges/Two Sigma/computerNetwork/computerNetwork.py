import numpy as np
from math import inf
from itertools import product

def create_nodemap(n, network):
    """ create a node map from list of bi-directional edge distances """
    # create an n x n node map set to infinity
    node_map = np.empty((n,n,))
    node_map[:] = inf
    # set bi-directional network distances into node map
    for node in network:
        i, j = node[0]-1, node[1]-1
        node_map[i, j] = node[2]
        node_map[j, i] = node[2]
    # set distance to self as 0
    for node in range(n):
        node_map[node, node] = 0
    return node_map

def computerNetwork(n, network):
    """ finds the minimum path from start node to end node """
    nodemap = create_nodemap(n, network)
    # relax edges based on Floyd-Warshall algorithm
    for iteration in range(n):
        for k, i, j in product(range(n), repeat=3):
            nodemap[i][j] = min(nodemap[i][j],
                                nodemap[i][k]+ nodemap[k][j])
    return nodemap[0][n-1]
