from typing import List, Set, Dict, Tuple

from typing import List
import math
import numpy as np

n = np.NaN

base_possibilities = {1,2,3,4,5,6,7,8,9}



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

def get_cube_bounds(array: List[List[int]],row,col,cube_size=3):
    row_min=math.floor(row/cube_size)
    col_min = math.floor(col / cube_size)

    return row_min*cube_size,(row_min+1)*cube_size,col_min*cube_size,(col_min+1)*cube_size

def get_cube_numbers(array: List[List[int]],row,col):
    #cube_bounds: 0: row_min, 1: row_max, 2: col_min, 3:col_max
    cube_bounds=get_cube_bounds(array,row,col)
    return {
        array[i,j]
            for i in range(cube_bounds[0],cube_bounds[1])
        for j in range(cube_bounds[2],cube_bounds[3])
        if not np.isnan(array[i,j])
    }

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


def get_possibilities(matrix: List[List[int]], row: int, col: int) -> Set[int]:
    possible = base_possibilities.copy()
    possible = possible.difference(matrix[row, :])
    possible = possible.difference(matrix[:, col])
    possible = possible.difference(get_cube_numbers(matrix, row, col))
    return possible


def get_all_field_possibilities(matrix: List[List[int]]) -> Dict[Tuple[int, int], Set[int]]:
    result = {}
    for i in range(0,9):
        for j in range(0,9):
            if np.isnan(matrix[i,j]):
                result[(i,j)] = get_possibilities(matrix, i,j)
    return result

def find_minimal_possible(possibs_dict: Dict[Tuple[int, int], Set[int]]) -> Tuple[Tuple[int,int], Set[int]]:
    chosen = None
    len_chosen = 10
    chosen_coord = None
    for coordinate, possib in possibs_dict.items():
        if len(possib) < len_chosen:
            chosen = possib
            len_chosen = len(chosen)
            chosen_coord = coordinate
        if len(chosen) == 0:
            raise ValueError("Not Solvable")
    return chosen_coord, chosen

def solver(matrix: List[List[int]]):
    input = matrix.copy()


possibs = get_all_field_possibilities(input)
chosen = find_minimal_possible(possibs)