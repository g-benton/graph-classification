import json
import numpy as np
import math
import sys
sys.path.append("../")

def read_star_wars():
    fpath = "/Users/greg/Google Drive/Spring 19/CS6241/graph-clustering/data/"
    fname = "star_wars_clean.json"

    ## BAD NODE = 76 ##
    with open(fpath+fname) as f:
        data = json.load(f)
        nodes = data['nodes']
        edges = data['links']

    # nodes[76]
    n_nodes = len(nodes)
    adj_mat = np.zeros((n_nodes, n_nodes))

    ## refactor edges ##
    for edge in edges:
        if edge['source'] > 76:
            edge['source'] -= 1
        if edge['target'] > 76:
            edge['target'] -= 1


    for edge in edges:
        adj_mat[edge['source'], edge['target']] = edge['value']
        adj_mat[edge['target'], edge['source']] = edge['value']

    nodes = [node['name'] for node in nodes]

    return adj_mat, nodes
