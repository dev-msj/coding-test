from operator import add

import pytest


def solution(map_size: str, move_str: str) -> str:
    n = int(map_size)
    move_list = move_str.split()
    
    # 내 코드
    # move_dict = {
    #     'L': (-1, 0),
    #     'R': (1, 0),
    #     'U': (0, -1),
    #     'D': (0, 1)
    # }
    
    # position = (1, 1)
    # for move in move_list:
    #     moved_position = tuple(map(add, position, move_dict.get(move)))
        
    #     if ((moved_position[0] < 1 or moved_position[0] > n) or (moved_position[1] < 1 or moved_position[1] > n)):
    #         continue
        
    #     position = moved_position
    
    # return f'{position[0]} {position[1]}'
    
    # 코파일럿 코드
    x = y = 1
    
    for move in move_list:
        if move == 'L' and x > 1:
            x -= 1
        elif move == 'R' and x < n:
            x += 1
        elif move == 'U' and y > 1:
            y -= 1
        elif move == 'D' and y < n:
            y += 1
    
    return f'{x} {y}'

@pytest.mark.parametrize("map_size, move_str, expected", [
    # 기본 테스트 케이스
    ("5", "R R R U D D", "4 3"),
    
    # 경계 테스트
    ("1", "L R U D", "1 1"),  # 1x1 공간에서 모든 방향 이동
    
    # 복합 이동 테스트
    ("4", "R R D D L L U U", "1 1"),  # 정사각형 이동 후 원점
    
    # 이동 없음
    ("5", "", "1 1"),                 # 빈 이동 문자열
])
def test_solution(map_size, move_str, expected):
    assert solution(map_size, move_str) == expected