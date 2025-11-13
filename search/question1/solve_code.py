import pytest


def solution(size: str, ice_box: list[str]) -> int:
    n, m = map(int, size.split())
    graph = []
    for i in range(n):
        print(i, ice_box[i])
        graph.append(list(map(int, ice_box[i])))
    
    def dfs(x, y):
        # 주어진 범위를 벗어나면 종료
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        
        # 방문하지 않은 노드면 방문 처리 후 상하좌우 탐색
        if graph[x][y] == 0:
            graph[x][y] = 1
            
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            
            # 탐색이 완료되면 카운트
            return True
        
        # 방문하지 않은 노드가 없으므로 카운팅하지 않음
        return False
    
    result = 0
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