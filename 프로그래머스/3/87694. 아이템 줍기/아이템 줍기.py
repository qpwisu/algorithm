from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표 2배로 확대 (대각선 이동 방지)
    board = [[0]*102 for _ in range(102)]

    # 1. 모든 사각형을 맵에 그리기
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1*2, x2*2+1):
            for j in range(y1*2, y2*2+1):
                board[i][j] = 1  # 내부 포함

    # 2. 테두리만 남기기 (내부 제거)
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1*2+1, x2*2):
            for j in range(y1*2+1, y2*2):
                board[i][j] = 0  # 내부 제거

    # 3. BFS
    visited = [[False]*102 for _ in range(102)]
    q = deque()
    q.append((characterX*2, characterY*2, 0))
    visited[characterX*2][characterY*2] = True

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while q:
        x, y, dist = q.popleft()
        if x == itemX*2 and y == itemY*2:
            return dist // 2  # 원래 크기로 환산

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 102 and 0 <= ny < 102:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))