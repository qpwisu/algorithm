from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for node in sorted(graph[start]):
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for next_node in sorted(graph[node]):
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True

# 입력 받기
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS와 BFS 결과 출력
visited = [False] * (N + 1)
dfs(graph, V, visited)
print()
bfs(graph, V)