import math
import numpy as np
import sys
sys.path.append("/Users/greg/Google Drive/Spring 19/CS6241/graph-clustering/spectral-clustering/")
from spectral_clustering import *
sys.path.append("/Users/greg/Google Drive/Spring 19/CS6241/graph-clustering/data/")
from read_star_wars import read_star_wars

def main():
    adj_mat, nodes = read_star_wars()
    n_clust = 30
    adj_mat.shape
    out = cluster(adj_mat, n_clust, normalized=True)
    groups = out[1]
    groups
    for clust in range(n_clust):
        inds = np.where(groups == clust)
        print("GROUP:")
        [print(nodes[ii]) for ii in list(inds[0])]
        print("\n\n")

if __name__ == '__main__':
    main()
