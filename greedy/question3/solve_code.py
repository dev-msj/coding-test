import pytest


def solution(condition_str) -> int:
    n, k = map(int, condition_str.split())
    
    count = 0
    while True:
        if n % k == 0:
            n = n // k
        else:
            n = n - 1
        
        count += 1
        
        if n == 1:
            break
    
    return count

@pytest.mark.parametrize("condition_str, expected", [
    ("2 2", 1),
    ("25 5", 2),
    ("100000 2", 21),
    ("10 3", 3),
])
def test_solution(condition_str, expected):
    assert solution(condition_str) == expected