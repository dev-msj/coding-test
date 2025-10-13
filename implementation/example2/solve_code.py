import pytest


def solution(n: str) -> int:
    one_min_cnt = 0
    for i in range(60):
        if "3" in str(i):
            one_min_cnt += 1
    
    one_hour_cnt = 0
    for i in range(60):
        if "3" in str(i):
            one_hour_cnt += 60
        else:
            one_hour_cnt += one_min_cnt
    
    total_cnt = 0
    for i in range(int(n) + 1):
        if "3" in str(i):
            total_cnt += 3600
        else:
            total_cnt += one_hour_cnt
    
    return total_cnt

    # 답안 예시
    # count = 0
    # for h in range(int(n) + 1):
    #     for m in range(60):
    #         for s in range(60):
    #             if '3' in f"{h}{m}{s}":
    #                 count += 1
    # return count

@pytest.mark.parametrize("n, expected", [
    ("0", 1575),
    ("2", 4725),
    ("3", 8325),
    ("5", 11475),
    ("9", 17775),
    ("13", 26100),
    ("15", 29250),
    ("17", 32400),
    ("21", 38700),
    ("23", 43875),
])
def test_solution(n, expected):
    assert solution(n) == expected