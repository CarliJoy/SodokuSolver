from typing import List

import numpy as np

n = np.NaN

def print_sodouk(array: List[List[int]]):
    for line_number, line, in enumerate(array):
        for row_number, val in enumerate(line):
            if val == np.NaN:
                val = " "
            else:
                print(f"{val}", end=" ")
            if row_number % 3:
                print("|", end="")
        if line_number % 3:
            print("-"*(len(line)+len(line)/3))
        print("")



input = np.array([
    [n, 3, n,  n, n, n,  n, n, n],
    [n, n, n,  1, 9, 5,  n, n, n],
    [n, n, 8,  n, n, n,  n, n, 6],
    [8, n, n,  n, 6, n,  n, n, n],
])

