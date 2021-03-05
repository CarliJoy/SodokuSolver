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

@pytest.mark.parametrize(
    "row,col,result",
    [
        (1, 1, {3,8}),
        (8, 8, {2,8,5,7}),
    ]
)
def test_cube_numbers(row, col, result):
    assert get_cube_numbers(test, row, col) == result

@pytest.mark.parametrize(
    "row,col,result",
    [
        (1, 0, {2,6,7}),
        (4, 6, {1,3,5,6,7,9}),
    ]
)
def test_cube_numbers(row, col, result):
    assert get_possibilities(test, row, col) == result

