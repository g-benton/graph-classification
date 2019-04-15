import math
import numpy as np
from scipy.cluster.vq import kmeans2
import matplotlib.pyplot as plt
import sys


def degree_matrix(W):
    """
    takes in adjacency matrix and returns the diagonal of the
    corresponding degree degree matrix
    """

    return np.sum(W, axis=0)

def laplacian_first_evecs(A, n_cluster, normalized=False):
    """
    computes the graph laplacian from an adjacency matrix
    """
    D = np.diag(degree_matrix(A))

    L = D - A
    if normalized:
        sqrt_inv_D = np.diag(1/np.diag(D))**(0.5)
        sqrt_inv_D[np.where(np.isinf(sqrt_inv_D))] = 0
        # L = sqrt_inv_D.matmul(L).matmul(sqrt_inv_D)
        L = np.matmul(np.matmul(sqrt_inv_D, L), sqrt_inv_D)
        # print(np.where(np.isnan(L)))

    w, v = np.linalg.eig(L)
    v = v[:, :n_cluster]
    if normalized:
        v = np.matmul(sqrt_inv_D, v)
        # v = sqrt_inv_D.matmul(v)
    return v

# def first_evecs(L, n_cluster=5, normalized=False):
#     w, v = np.linalg.eig(L)
#     if normalized:
#         return
#     return v[:, :n_cluster]

def cluster(A, n_cluster=5, normalized=False):
    V = laplacian_first_evecs(A, n_cluster, normalized)
    # U = first_evecs(L, n_cluster, normalized)
    # return U
    clusters = kmeans2(V, n_cluster, iter=20000)
    return clusters
