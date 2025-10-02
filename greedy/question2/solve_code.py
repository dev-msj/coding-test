from typing import List

import pytest


def solution(size_str: str, card_str_list: List[str]) -> int:
    n, m = map(int, size_str.split())
    max_card = 0
    
    for i in range(n):
        card_info_list = list(map(int, card_str_list[i].split()))
        for card_list in card_info_list:
            min_card = min(card_list)
            if max_card < min_card:
                max_card = min_card
    
    return max_card

@pytest.mark.parametrize("size_str, card_rows, expected", [
    # N=3, M=3, rows: [3,1,2], [4,1,4], [2,2,2] -> mins [1,1,2] -> max 2
    ("3 3", ["3 1 2", "4 1 4", "2 2 2"], 2),
    # N=1, M=1
    ("1 1", ["5"], 5),
    # all same
    ("2 2", ["7 7", "7 7"], 7),
    # N=4, M=3 -> rows -> mins [1,2,7,1] -> max 7
    ("4 3", ["5 1 3", "2 4 6", "9 8 7", "1 2 3"], 7),
    # N=3, M=4 -> mins [1,3,1] -> max 3
    ("3 4", ["1 9 8 7", "6 5 4 3", "2 1 1 1"], 3),
])
def test_solution(size_str, card_rows, expected):
    assert solution(size_str, card_rows) == expected