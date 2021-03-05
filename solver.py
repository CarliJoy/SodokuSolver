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

def get_line()

def get_poss_number(array: List[List[int]],row,col):
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            print(array[i,j])



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


])

get_poss_number(input,1,1)
