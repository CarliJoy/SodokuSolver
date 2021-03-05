from typing import List
import math
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

def get_cube_bounds(array: List[List[int]],row,col,cube_size):
    cube_bounds=array[0,0,0,0]
    #get value between 0 and 1
    row_min=array.shape[0]/row
    #multiply with cubesize and floor
    row_min=math.floor(row_min*cube_size)

def cube_number(array: List[List[int]],row,col):
    #cube_bounds: 0: row_min, 1: row_max, 2: col_min, 3:col_max
    cube_bounds=array[0,0,0,0]
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
],
    np.float16
)

get_poss_number(input,1,1)
