n, m = map(int, input().split())
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

distance = [float('inf') for _ in range(n+1)]
distance[1] = 0
# n-1번 반복하면서 모든 간선을 확인하고, 최단 거리를 갱신
for i in range( n-1):
    for u,v,w in edges:
        if distance[v] > distance[u] + w:
            distance[v] = distance[u] + w

has_negative_cycle = False
# 한번더 갱신해서 음수가 존재하면 음의 사이클 존재
for u, v, w in edges:
    if distance[u] != float('inf') and distance[u] + w < distance[v]:
        has_negative_cycle = True
        break

if has_negative_cycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if distance[i] == float('inf'):
            print(-1)
        else:
            print(distance[i])