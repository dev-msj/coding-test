import pytest


def solution(input: str) -> int:
    count = 0
    # to_number_dict = {
    #     'a': 1,
    #     'b': 2,
    #     'c': 3,
    #     'd': 4,
    #     'e': 5,
    #     'f': 6,
    #     'g': 7,
    #     'h': 8,
    # }
    coordinate = [
        # int(to_number_dict[input[0]]),
        ord(input[0]) - ord('a') + 1,
        int(input[1])
    ]
    move_list = [
        [2, 1], [2, -1], [-2, 1], [-2, -1],
        [1, 2], [1, -2], [-1, 2], [-1, -2]
    ]
    
    for move in move_list:
        x = coordinate[0] + move[0]
        y = coordinate[1] + move[1]
        
        if 0 < x < 9 and 0 < y < 9:
            count += 1
    
    return count

@pytest.mark.parametrize('input, expected', [
    ("a1", 2),
    ("c2", 6),
    ("e4", 8)
])
def test_solution(input, expected):
    assert solution(input) == expected