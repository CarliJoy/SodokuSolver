import numpy as np
from solver import get_possibilities, get_cube_bounds, get_cube_numbers

n = np.NaN


test = np.array([
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

assert get_cube_numbers(test,1,1)== {3,8}
assert get_possibilities(test, 0, 0) == {1,2,5,6,7,9}
assert get_possibilities(test, 1, 0) == {2,6,7}
