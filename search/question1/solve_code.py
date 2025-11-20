import pytest


def solution(size: str, ice_box: list[str]) -> int:
    n, m = map(int, size.split())
    grid_graph = []
    for i in range(n):
        grid_graph.append(list(map(int, ice_box[i])))
    
    def dfs(x: int, y: int) -> bool:
        # 격자 범위를 벗어나면 탐색 종료
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        
        # 방문하지 않은 노드(구멍 뚫린 칸)이면 방문 처리 후 상하좌우 탐색
        if grid_graph[x][y] == 0:
            # 방문 처리
            grid_graph[x][y] = 1
            
            # 인접 노드 탐색
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            
            # 탐색이 완료되면 아이스크림 카운트
            return True
        
        # 이미 방문했거나 칸막이 노드(1)인 경우 카운트하지 않음
        return False
    
    result = 0
    # 격자 그래프 노드의 모든 좌표를 직접 순회하며 dfs 수행
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
    
    return result

@pytest.mark.parametrize("size, ice_box, expected", [
    ("3 3", ["001", "111", "000"], 2),
    ("4 5", ["00110", "00011", "11111", "00000"], 3)
])
def test_solution(size: str, ice_box: list[str], expected: int):
    assert solution(size, ice_box) == expected