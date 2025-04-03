from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()
queue.append((0, 0))
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            if graph[ny][nx] == 1 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx, ny))

print(visited[N - 1][M - 1])