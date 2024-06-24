from collections import deque
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    graph = []
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    for i in range(N):
        line = list(map(int, list(input())))
        graph.append(line)
    weight = [[float("inf")]* N for _ in range(N)] # 가중치
    q = deque()
    q.append([0,0])
    weight[0][0] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx <N  and 0<=ny <N: # 그래프내 범위 벗어 난 경우
                if weight[x][y]+graph[nx][ny] < weight[nx][ny]:
                    q.append([nx, ny])
                    weight[nx][ny] = weight[x][y]+graph[nx][ny]
    print(f'#{test_case} {weight[N-1][N-1]}')
