import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    graph[x][y] = 0  # 방문한 섬은 0으로 표시해서 다시 방문하지 않도록 함
    
    for i in range(8):  # 8방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:  # 입력의 끝
        break
    
    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:  # 섬을 발견하면 DFS 실행
                dfs(i, j)
                count += 1
    
    print(count)