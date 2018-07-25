import max_min_diversity


if __name__ == '__main__':

    det_set = max_min_diversity.compute_diverse_set('./temp_ssn_identities.npy',
                                            'temp_ssn_headings.json', 60)

    trials = 1

    for i in range(0, trials):

        stoch_set = max_min_diversity.compute_diverse_set(
                './temp_ssn_identities.npy','temp_ssn_headings.json', 60, True)

        comb_set = set(det_set + stoch_set)

        print len(comb_set)

    # max_min_diversity.compute_diverse_set('./temp_csn_identities.npy',
    #                                         'temp_csn_headings.json', 60, True)
