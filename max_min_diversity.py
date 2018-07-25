import numpy as np
import data_prep

def greedy_min_max_alg(dist, headings, set, k, stochastic=False):

        while len(set) < k:

            min_val = 10
            min_ind = 0

            for i in range(0, len(dist)):

                if i in set:
                    continue

                rand = np.random.randint(0,10000)

                if stochastic and rand < 3:

                    print 'RANDOM ADDITION: ' + str(rand)
                    min_ind = i
                    break

                max_val = np.nanmax(dist[i])

                if max_val < min_val:

                    min_val = max_val
                    min_ind = i

            print "ADDED %s" % (headings[min_ind])

            set += [min_ind]

        return set



def compute_diverse_set(dist_file, heading_file, k, stochastic=False):

    set = []

    dist = data_prep.initialise_matrix(dist_file)

    headings = data_prep.initialise_headings(heading_file)
    #
    # dist = data_prep.initialise_matrix('./temp_ssn_identities.npy')
    #
    # headings = data_prep.initialise_headings('temp_ssn_headings.json')
    #
    # dist = data_prep.initialise_matrix('./temp_csn_identities.npy')
    #
    # headings = data_prep.initialise_headings('temp_csn_headings.json')

    min = data_prep.get_matrix_min(dist)

    print "MIN: %s-%s" % (headings[min[0]], headings[min[1]])

    set += [min[0], min[1]]

    # set += [np.random.randint(0,241)]
    #
    # set += [np.random.randint(0,241)]


    set = greedy_min_max_alg(dist, headings, set, k, stochastic)

    set = sorted([headings[x] for x in set])

    print set
