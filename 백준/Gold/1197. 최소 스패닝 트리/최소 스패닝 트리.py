'''
3 3
1 2 1
2 3 2
1 3 3

최소신장트리 Prim
주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
우선순위 큐
하나씩 넣어서 (가중치, 출발점)

'''

import heapq
from collections import defaultdict

V,E = map(int,input().split())
graph = defaultdict(list)

for i in range(E):
    tmp = list(map(int,input().split()))
    graph[tmp[0]].append([tmp[1],tmp[2]])
    graph[tmp[1]].append([tmp[0],tmp[2]])

visited = [False] * (V+1)
pq = [[0,1]]
n = 0
cost = 0
while pq and n < V:
    w,v = heapq.heappop(pq)
    if visited[v]:
        continue
    visited[v] = True
    n+=1
    cost += w
    for i,j in graph[v]:
        if not visited[i]:
            heapq.heappush(pq,[j,i])

print(cost)