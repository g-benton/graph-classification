import math
import numpy as np
from scipy.cluster.vq import kmeans2
import matplotlib.pyplot as plt
import sys
from k_means import kmeans


def degree_matrix(W):
    """
    takes in adjacency matrix and returns the diagonal of the
    corresponding degree degree matrix
    """

    return np.sum(W, axis=1)

def laplacian_first_evecs(A, n_cluster, normalized=False):
    """
    computes the graph laplacian from an adjacency matrix
    """
    D = np.diag(degree_matrix(A))
    # print(1/np.diag(D))
    L = D - A

    if normalized:
        sqrt_inv_D = np.diag(np.diag(D)**(-0.5))
        # print(np.matmul(sqrt_inv_D, sqrt_inv_D))
        L = np.matmul(np.matmul(sqrt_inv_D, L), sqrt_inv_D)

    w, v = np.linalg.eig(L)
    v = v[:, :n_cluster]
    if normalized:
        v = np.matmul(sqrt_inv_D, v)
    return v


def cluster(A, n_cluster=5, normalized=False):
    V = laplacian_first_evecs(A, n_cluster, normalized)
    # U = first_evecs(L, n_cluster, normalized)
    # return U
    # print(V.shape)
    # clusters = kmeans2(V, n_cluster, iter=20000)
    clusters = kmeans(V, n_cluster, niters=2000)
    return clusters
