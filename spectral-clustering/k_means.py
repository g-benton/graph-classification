import math
import numpy as np
import matplotlib.pyplot as plt

class node():
    """docstring for node."""
    def __init__(self, pos, original_ind):
        self.pos = pos

        self.label = original_ind
        self.centroid = None

class centroid():
    """docstring for centroid."""
    def __init__(self, pos, id):
        self.pos = pos
        self.id = id


def get_dist(node, centroid):
    return np.linalg.norm(node.pos - centroid.pos)

def compute_new_center(node_positions):
    avg_pos = np.mean(node_positions, 0)
    return avg_pos


def update_assignments(node_list, centroids):
    ## look through list and get distances to all centroids for all nodes ##
    for node in node_list:
        min_dist = None
        for centroid in centroids:
            dist = get_dist(node, centroid)
            if min_dist is None:
                min_dist = dist
                node.centroid = centroid.id
            elif dist < min_dist:
                min_dist = dist
                node.centroid = centroid.id

    return node_list


def update_centroid_centers(node_list, centroids):
    # print("n centr = ", len(centroids))
    for centroid in centroids:
        has_node = False
        # just a temporary place holder #
        node_positions = centroid.pos
        for node in node_list:
            if node.centroid == centroid.id:
                has_node = True
                node_positions = np.vstack((node_positions, node.pos))

        # only update if there are any nodes in the centroid #
        if has_node:
            centroid.pos = compute_new_center(node_positions[1:, ])

    return centroids

def kmeans(node_mat, n_clusters, niters=100):
    ## set up everything ##
    n_dim = node_mat.shape[1]

    # random centroids #
    start_centers = np.random.rand(n_clusters, n_dim)*0.1 - 0.05
    centroids = [centroid(start_centers[ii, :], ii) for ii in range(n_clusters)]
    # node list #
    node_list = []
    for rr in range(node_mat.shape[0]):
        node_list.append(node(node_mat[rr, :], rr))

    for ii in range(niters):
        node_list = update_assignments(node_list, centroids)
        centroids = update_centroid_centers(node_list, centroids)

    return node_list, centroids
