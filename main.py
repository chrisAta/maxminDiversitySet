import numpy as np
import data_prep

if __name__ == '__main__':

    set = []

    k = 60

    dist = data_prep.initialise_matrix('./temp_csn_identities.npy')

    headings = data_prep.initialise_headings('temp_csn_headings.json')

    min = data_prep.get_matrix_min(dist)

    print "MIN: %s-%s" % (headings[min[0]], headings[min[1]])

    set += [min[0], min[1]]

    # set += [np.random.randint(0,241)]
    #
    # set += [np.random.randint(0,241)]


    set = data_prep.greedy_min_max_alg(dist, headings, set, k)

    print [headings[x] for x in set]
