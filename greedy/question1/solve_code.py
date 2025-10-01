import pytest


def solution(input_condition_string: str, input_int_string: str) -> int:
    input_condition_string_list = [int(i) for i in input_condition_string.split()]
    input_int_list = [int(i) for i in input_int_string.split()]
    input_int_list.sort()

    m = input_condition_string_list[1]
    k = input_condition_string_list[2]
    max_value = input_int_list[-1]
    sec_value = input_int_list[-2]

    # result = ((m // k) * (max_value * k)) + ((m % k) * sec_value)
    result = 0
    
    while True:
        # 가장 큰 수를 k번 더하기
        for i in range(k):
            if m == 0:
                break
            
            result += max_value
            m-= 1
        
        if m == 0:
            break
        
        result += sec_value
        m -= 1

    return result

@pytest.mark.parametrize("cond, arr, expected", [
    ('5 8 3', '2 4 5 4 6', 46),
    ('2 2 3', '6 5', 12),
    ('3 5 2', '3 3 3', 15),
    ('2 4 1', '6 5', 22),
])
def test_solution(cond, arr, expected):
    assert solution(cond, arr) == expected
