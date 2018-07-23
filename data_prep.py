import numpy as np
import json

def read_matrix(dist_file, heading_file):

    dist = np.load(dist_file)

    with open(heading_file) as heading:
        headings = json.loads(heading.read())

    return (dist, headings)
