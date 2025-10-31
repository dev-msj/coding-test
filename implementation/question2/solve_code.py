import pytest


def solution(map_size_str: str, charactor_info_str: str, map_value_list: list[str]) -> int:
    result = 0
    move_dict = {
        0: (0, -1),
        1: (1, 0),
        2: (0, 1),
        3: (-1, 0)
    }
    
    n, m = map(int, map_size_str.split())
    game_map = [[0] * n for _ in range(m)]
    a, b, d = map(int, charactor_info_str.split())
    coordinate = (a, b)
    
    for i, values_str in enumerate(map_value_list):
        map_values = list(map(int, values_str.split()))
        for j, value in enumerate(map_values):
            game_map[i][j] = value
    
    turn_cnt = 0
    while(True):
        if turn_cnt == 4:
            d = (d + 2) % 4
        else:
            d = (d + 3) % 4
        turn_cnt += 1
        
        move = tuple(x + y for x, y in zip(coordinate, move_dict[d]))
        if game_map[move[0]][move[1]] == 0:
            result += 1
            coordinate = move
            turn_cnt = 0
            game_map[move[0]][move[1]] = 1
        elif turn_cnt > 4:
                break
    
    return result

def answer(map_size_str: str, charactor_info_str: str, map_value_list: list[str]) -> int:
    # N, M을 공백을 기준으로 구분하여 입력받기
    n, m = map(int, map_size_str.split())

    # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
    d = [[0] * m for _ in range(n)]
    # 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
    x, y, direction = map(int, charactor_info_str.split())
    d[x][y] = 1 # 현재 좌표 방문 처리

    # 전체 맵 정보를 입력받기
    array = []
    for values in map_value_list:
        array.append(list(map(int, values.split())))

    # 북, 동, 남, 서 방향 정의
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 왼쪽으로 회전
    def turn_left():
        global direction
        direction -= 1
        if direction == -1:
            direction = 3

    # 시뮬레이션 시작
    count = 1
    turn_time = 0
    while True:
        # 왼쪽으로 회전
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        else:
            turn_time += 1
        # 네 방향 모두 갈 수 없는 경우
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            # 뒤로 갈 수 있다면 이동하기
            if array[nx][ny] == 0:
                x = nx
                y = ny
            # 뒤가 바다로 막혀있는 경우
            else:
                break
            turn_time = 0

    # 정답 출력
    return count

@pytest.mark.parametrize("map_size_str, charactor_info_str, map_value_list, expected", [
    ('4 4', '1 1 0', ['1 1 1 1', '1 0 0 1', '1 1 0 1', '1 1 1 1'], 3)
])
def test_solution(map_size_str: str, charactor_info_str: str, map_value_list: list[str], expected: int):
    assert solution(map_size_str, charactor_info_str, map_value_list) == expected