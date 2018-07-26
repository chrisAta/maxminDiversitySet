import max_min_diversity


if __name__ == '__main__':

    ssn_set = max_min_diversity.compute_diverse_set('./temp_ssn_identities.npy',
                                            'temp_ssn_headings.json',140)


    csn_set = max_min_diversity.compute_diverse_set(
                './temp_csn_identities.npy','temp_csn_headings.json', 140)

    comb_set = set(ssn_set + csn_set)

    print len(comb_set)

    # max_min_diversity.compute_diverse_set('./temp_csn_identities.npy',
    #                                         'temp_csn_headings.json', 60, True)
