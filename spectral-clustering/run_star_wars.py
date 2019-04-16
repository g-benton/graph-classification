import math
import numpy as np
import sys
sys.path.append("/Users/greg/Google Drive/Spring 19/CS6241/graph-clustering/spectral-clustering/")
from spectral_clustering import *
sys.path.append("/Users/greg/Google Drive/Spring 19/CS6241/graph-clustering/data/")
from read_star_wars import read_star_wars

def main():
    # np.random.seed(416)
    np.random.seed(8818)
    adj_mat, nodes = read_star_wars()
    n_clust = 7
    adj_mat.shape

    # run with homemade k means ##
    node_list, clusters = cluster(adj_mat, n_clust, normalized=True)
    groups = np.array([n.centroid for n in node_list])
    # print([n.pos for n in node_list])
    # groups
    for clust in range(n_clust):
        inds = np.where(groups == clust)
        print("GROUP:")
        [print(nodes[ii]) for ii in list(inds[0])]
        print("\n\n")

if __name__ == '__main__':
    main()
