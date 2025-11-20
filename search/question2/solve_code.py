from collections import deque
import pytest


def solution(map_size: str, monster_info: list[str]) -> int:
    n, m = map(int, map_size.split())
    grid_graph = []
    for i in range(n):
        grid_graph.append(list(map(int, monster_info[i])))
    
    def bfs(x, y):
        queue = deque([(x, y)])
        
        while queue:
            x, y = queue.popleft()
            
            # 도착점 도달
            if x == m - 1 and y == n - 1:
                return grid_graph[y][x]
            
            # 상하좌우 탐색
            for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nx, ny = x + dx, y + dy
                
                # 범위 체크 및 이동 가능한 칸(1) 확인
                if 0 <= nx < m and 0 <= ny < n and grid_graph[ny][nx] == 1:
                    # 시작 위치로부터의 거리 누적 계산
                    grid_graph[ny][nx] = grid_graph[y][x] + 1
                    queue.append((nx, ny))
    
    # def bfs(x, y):
    #     # 첫 방문은 이동으로 처리하지 않음
    #     count = -1
    #     queue = deque([(x, y)])
        
    #     while True:
    #         x, y = queue.popleft()
            
    #         grid_graph[y][x] = 0
    #         count += 1
            
    #         if x == m - 1 and y == n - 1:
    #             return count
            
    #         # 위로 이동 가능하며 괴물이 없음
    #         if y + 1 < n and grid_graph[y + 1][x] == 1:
    #             queue.append((x, y + 1))
            
    #         # 아래로 이동 가능하며 괴물이 없음
    #         if y - 1 >= 0 and grid_graph[y - 1][x] == 1:
    #             queue.append((x, y - 1))
            
    #         # 좌로 이동 가능하며 괴물이 없음
    #         if x - 1 >= 0 and grid_graph[y][x - 1] == 1:
    #             queue.append((x - 1, y))
            
    #         # 우로 이동 가능하며 괴물이 없음
    #         if x + 1 < m and grid_graph[y][x + 1] == 1:
    #             queue.append((x + 1, y))
    
    return bfs(0, 0)

@pytest.mark.parametrize("map_size, monster_info, expected", [
    ("5 6", ["101010", "111111", "000001", "111111", "111111"], 10),
])
def test_solution(map_size: str, monster_info:list[str], expected: int):
    assert solution(map_size, monster_info) == expected