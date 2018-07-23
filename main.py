from data_prep import read_matrix

if __name__ == '__main__':

    (dist, headings) = read_matrix('./temp_ssn_identities.npy', 'temp_ssn_headings.json')

    print dist
    print headings
