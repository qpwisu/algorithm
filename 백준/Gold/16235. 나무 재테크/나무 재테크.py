def spring():
    dead =[ [0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tree = graph[i][j]
            f = food[i][j]
            tree.sort()
            tmp = []
            for t in tree:
                nf = f - t
                if nf < 0 :
                    dead[i][j] += t // 2
                else :
                    f = nf
                    tmp.append(t+1)

            graph[i][j] = tmp
            food[i][j] = f

    # summer
    for i in range(n):
        for j in range(n):
            food[i][j] += dead[i][j]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, +1, -1, 1, -1, 0, 1]

# 가을
def fall():

    for i in range(n):
        for j in range(n):

            for t in graph[i][j]:
                if t % 5 == 0:
                    for h in range(8):
                        nx = i + dx[h]
                        ny = j + dy[h]

                        if nx < 0 or nx >= n or ny < 0 or ny >= n :
                            continue

                        graph[nx][ny].append(1)

# 겨울
def winter():
    for i in range(n):
        for j in range(n):
            food[i][j] += A[i][j]

n, m, k = map(int,input().split())

A = []

for _ in range(n):
    A.append(list(map(int,input().split())))

# 현재 양분
food = [[5] * n for _ in range(n)]
# 심겨진 나무
graph = [ [[] for _ in range(n)] for _ in range(n) ]

for _ in range(m):
    x, y, z = map(int,input().split())
    graph[x-1][y-1].append(z)

for _ in range(k):
    spring()

    fall()

    winter()

ans = 0

for i in range(n):
    for j in range(n):
        ans += len(graph[i][j])

print(ans)
