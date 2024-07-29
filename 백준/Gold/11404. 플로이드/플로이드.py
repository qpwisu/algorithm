n = int(input())
m = int(input())

edge = []
for _ in range(m):
    edge.append(list(map(int,input().split())))

graph = [[float('inf')] *(n+1) for _ in range(n+1)]

for s,e,d in edge:
    # 하나의 경로가 여러개 있을 수 있음
    if graph[s][e] != float('inf') and graph[s][e] < d :
        continue
    graph[s][e] = d

# 자기 자신에게 이동은 0
for i in range(1,n+1):
    graph[i][i] = 0
# i->j 까지 가는 경로의 거리가 i->k + k->j 의 합보다 크면 바꿔줘야함

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1,n+1):
    for j in range(1, n+1):
        if graph[i][j] == float('inf'):
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

