from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표를 두 배로 확대하여 반쪽 좌표 문제를 해결
    def expand(coords):
        return [2 * c for c in coords]
    
    characterX, characterY, itemX, itemY = expand([characterX, characterY, itemX, itemY])
    rectangle = [expand(rect) for rect in rectangle]

    graph = [[-1] * 102 for _ in range(102)]
    
    # 도형의 테두리를 그리기
    for rect in rectangle:
        x1, y1, x2, y2 = rect
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    graph[y][x] = 0  # 내부 부분
                elif graph[y][x] != 0:
                    graph[y][x] = 1  # 테두리 부분
    
    # BFS를 사용하여 최단 거리 찾기
    queue = deque([(characterX, characterY, 0)])
    visited = [[False] * 102 for _ in range(102)]
    visited[characterY][characterX] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y, count = queue.popleft()
        
        if x == itemX and y == itemY:
            return count // 2  # 좌표를 두 배로 확대했으므로 결과를 나누어줍니다.

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < 102 and 0 <= ny < 102 and graph[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny, count + 1))
    
    return 0  # 도달 불가한 경우

