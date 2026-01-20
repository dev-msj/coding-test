import pytest


def solution(int_arr: list[int]) -> list[int]:
    if len(int_arr) <= 1:
        return int_arr
    
    pivot = int_arr[0]
    tail = int_arr[1:]
    
    left_arr = [y for y in tail if y > pivot]
    right_arr = [x for x in tail if x <= pivot]
    
    return solution(left_arr) + [pivot] + solution(right_arr)

@pytest.mark.parametrize("int_arr, expected", [
    ([15, 27, 12], [27, 15, 12]),
    ([13, 2, 33, 24, 57], [57, 33, 24, 13, 2]),
    ([10], [10]),
    ([], []),
    ([2, 1, 0, 2], [2, 2, 1, 0]),
])
def test_solution(int_arr, expected):
    assert solution(int_arr) == expected