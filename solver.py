#!/usr/bin/env python
from pathlib import Path
from typing import List, Set, Dict, Tuple
import sys
from typing import List
import math
import numpy as np
from reader import read_excel
from writer import write_result

n = np.NaN

base_possibilities = {1,2,3,4,5,6,7,8,9}

class SolutionNotFound(ValueError):
    pass


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

input_matrix = np.array([
    [n, 3, n,  n, n, n,  n, n, n],
    [n, n, n,  1, 9, 5,  n, n, n],
    [n, n, 8,  n, n, n,  n, n, 6],
    [8, n, n,  n, 6, n,  n, n, n],
    [4, n, n,  8, n, n,  n, n, 1],
    [n, n, n,  n, 2, n,  n, n, n],
    [n, 6, n,  n, n, n,  2, 8, n],
    [n, n, n,  4, 1, 9,  n, n, 5],
    [n, n, n,  n, n, n,  n, 7, n]
],
    np.float16
)

solution_matrix = np.array([
    [5, 3, 4,  6, 7, 8,  9, 1, 2],
    [6, 7, 2,  1, 9, 5,  3, 4, 8],
    [1, 9, 8,  3, 4, 2,  5, 6, 7],
    [8, 5, 9,  7, 6, 1,  4, 2, 3],
    [4, 2, 6,  8, 5, 3,  7, 9, 1],
    [7, 1, 3,  9, 2, 4,  8, 5, 6],
    [9, 6, 1,  5, 3, 7,  2, 8, 4],
    [2, 8, 7,  4, 1, 9,  6, 3, 5],
    [3, 4, 5,  2, 8, 6,  1, 7, 9],
])

test1 = np.array([
    [5, 3, n,  n, 7, n,  n, n, n],
    [6, n, n,  1, 9, 5,  n, n, n],
    [n, 9, 8,  n, n, n,  n, 6, n],
    [8, n, n,  n, 6, n,  n, n, 3],
    [4, n, n,  8, n, 3,  n, n, 1],
    [7, n, n,  n, 2, n,  n, n, 6],
    [n, 6, n,  n, n, n,  2, 8, n],
    [n, n, n,  4, 1, 9,  n, n, 5],
    [n, n, n,  n, 8, n,  n, 7, 9],
])

test2 = np.array([
    [n, 3, n,  n, 7, n,  n, n, n],
    [6, n, n,  1, 9, 5,  n, n, n],
    [n, 9, 8,  n, n, n,  n, 6, n],
    [8, n, n,  n, 6, n,  n, n, 3],
    [4, n, n,  8, n, 3,  n, n, 1],
    [7, n, n,  n, 2, n,  n, n, 6],
    [n, 6, n,  n, n, n,  2, 8, n],
    [n, n, n,  4, 1, 9,  n, n, 5],
    [n, n, n,  n, 8, n,  n, 7, 9],
])


def get_possibilities(matrix: List[List[int]], row: int, col: int) -> Set[int]:
    possible = base_possibilities.copy()
    possible = possible.difference(matrix[row, :])
    possible = possible.difference(matrix[:, col])
    possible = possible.difference(get_cube_numbers(matrix, row, col))
    return possible


def get_all_field_possibilities(matrix: List[List[int]]) -> Dict[Tuple[int, int], Set[int]]:
    result = dict()
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
            raise SolutionNotFound("Not Solvable")
    return chosen_coord, chosen

def solver(matrix: List[List[int]], possibs_matrix: Dict[Tuple[int, int], Set[int]] = None) -> List[List[int]]:

    if possibs_matrix is None:
        possibs_matrix = get_all_field_possibilities(matrix)

    # Kleinstes Möglichkeitsset finde
    coord, possibs = find_minimal_possible(possibs_matrix)

    # Für jede Möglichkeit den Solver nochmal ausführen, rekursiv
    for possib in possibs:
        try:
            # Kopie erstellen vom Original
            new_try = matrix.copy()
            new_try[coord[0], coord[1]] = possib
            new_try_possibs_matrix = get_all_field_possibilities(new_try)
            if len(new_try_possibs_matrix) == 0:
                return new_try
            return solver(new_try, new_try_possibs_matrix)
        except SolutionNotFound:
            pass
    raise SolutionNotFound("In the Main Solver no solution was found")


def get_solved_path(path: Path):
    folder = path.absolute().parent
    return folder / f"{path.stem}_solved{path.suffix}"


def run(filename: str):
    filename = Path(filename)
    print(f"** Reading: {filename}")
    print(" ** Trying to solve: ")
    source = read_excel(filename)
    print_sodouk(source)
    try:
        solution = solver(source)
        print("** Solved: ")
        print_sodouk(solution)
        solved_path = get_solved_path(filename)
        print(f"Writing solution to {solved_path}")
        write_result(filename, solution, solved_path)
    except SolutionNotFound:
        print("** No solution found")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        print("Program except only one value, the path to the excel input")
