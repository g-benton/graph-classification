import numpy as np
import math
import sys
import re
sys.path.append("/Users/greg/Google Drive/Spring 19/CS6241/graph-clustering/data/")
sys.path.append("../spectral-clustering/")
from spectral_clustering import *

def main():
    ## generate the list of names to keep ##
    keep_fname = "keep_list.txt"
    with open(keep_fname) as ins:
        keep_list = []
        for line in ins:
            # keep_list.append(re.sub('"|\n', '', line))
            keep_list.append(line)

    ## get all the numbers out of the master list ##
    hero_fname = "marvel.txt"
    hero_count = 0
    with open(hero_fname) as ins:
        hero_names = []
        hero_nums = []
        for line in ins:
            hero_count += 1

            line = line.split(" ", 1)
            h_num = line[0]
            h_name = line[1]
            if h_name in keep_list:
                hero_nums.append(int(h_num))
                hero_names.append(h_name)

    ## generate the adjacency matrix ##
    adj_mat = np.zeros((hero_count, hero_count), int)

    # get out list of comics for each hero #
    edge_fname = "edge_list.txt"
    keep_comics = []
    with open(edge_fname) as ins:
        for line in ins:
            line = line.split()
            if int(line[0]) in hero_nums:
                line = [int(l) for l in line]
                keep_comics.append(line[1:])

    # go through all comics by hero #
    for h1_ind, h1_num in enumerate(hero_nums):
        for h2_ind, h2_num in enumerate(hero_nums):
            for comic in keep_comics[h1_ind]:
                if comic in keep_comics[h2_ind]:
                    # print(h1_num)Vj
                    # print(h2_num)
                    adj_mat[h1_num, h2_num] = 1
                    adj_mat[h2_num, h1_num] = 1

    # get out the adj mat where we want #
    cols = np.tile(hero_nums, (len(hero_nums), 1))
    adj_mat = adj_mat[cols.transpose(), cols]
    print(adj_mat)
    print(hero_nums)
    print(hero_names)


x = np.arange(20).reshape(5, 4)
x

row = np.tile([1,3], (2,1))
row

x[row, row.transpose()]



    # out = cluster(adj_mat, 100)




if __name__ == '__main__':
    main()

test = np.random.rand(3,3)
test
inds = [0,2]
test[1, inds] = 1
test
