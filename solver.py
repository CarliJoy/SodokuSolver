from typing import List

import numpy as np

n = np.NaN

def print_sodouk(array: List[List[int]]):
    print("-" * (9 * 3- 2))
    for line_number, line, in enumerate(array, start=1):
        print("|", end=" ")
        for row_number, val in enumerate(line, start=1):
            if np.isnan(val):
                print(" ", end=" ")
            else:
                print(f"{val:1.0f}", end=" ")
            if row_number % 3 == 0:
                print("|", end=" ")
        print("")
        if line_number % 3 == 0:
            print("-"*(9*3-2))



input = np.array([
    [n, 3, n,  n, n, n,  n, n, n],
    [n, n, n,  1, 9, 5,  n, n, n],
    [n, n, 8,  n, n, n,  n, n, 6],
    [8, n, n,  n, 6, n,  n, n, n],
    [4, n, n,  8, n, n,  n, n, n],
    [n, n, n,  n, 2, n,  n, n, n],
    [n, 6, n,  n, n, n,  2, 8, n],
    [n, n, n,  4, 1, 9,  n, n, 5],
    [n, n, n,  n, 6, n,  n, 7, n]
],
    np.float16
)


