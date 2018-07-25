import numpy as np
import pandas
import json

def initialise_matrix(dist_file):

    dist = np.load(dist_file)

    for i in range(0, len(dist)):
        dist[i][i] = np.nan

    return np.asmatrix(dist)

def initialise_headings(heading_file):

    with open(heading_file) as heading:
        headings = json.loads(heading.read())

    temp_dict = {}

    for i in range(0, len(headings)):
        temp_dict[i] = headings[i]

    return temp_dict

def get_matrix_min(dist):

    min_arr = np.where(dist == np.nanmin(dist))

    return min_arr[0]

def greedy_min_max_alg(dist, headings, set, k):

        while len(set) < k:

            min_val = 10
            min_ind = 0

            for i in range(0, len(dist)):

                if i in set:
                    continue

                rand = np.random.randint(0,10000)

                #COMMENT THIS OUT FOR DETERMINISTIC
                # if rand < 3:
                #
                #     print 'RANDOM ADDITION: ' + str(rand)
                #     min_ind = i
                #     break

                max_val = np.nanmax(dist[i])

                if max_val < min_val:

                    min_val = max_val
                    min_ind = i

            print "ADDED %s" % (headings[min_ind])

            set += [min_ind]

        return set
