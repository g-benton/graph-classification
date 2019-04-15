import json
import numpy as np
import math
import sys
sys.path.append("../")

def read_star_wars():
    fpath = "/Users/greg/Google Drive/Spring 19/CS6241/graph-clustering/data/"
    fname = "star_wars.json"


    with open(fpath+fname) as f:
        data = json.load(f)
        nodes = data['nodes']
        edges = data['links']

    n_nodes = len(nodes)
    adj_mat = np.zeros((n_nodes, n_nodes))

    for edge in edges:
        # adj_mat[edge['source'], edge['target']] = edge['value']
        # adj_mat[edge['target'], edge['source']] = edge['value']
        adj_mat[edge['source'], edge['target']] = 1
        adj_mat[edge['target'], edge['source']] = 1

    nodes = [node['name'] for node in nodes]

    return adj_mat, nodes
