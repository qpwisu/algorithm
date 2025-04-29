import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**6)

N, M, X = map(int, input().split())

dic = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

for key in dic.keys():
    dic[key].sort()

answer = []

# DFS
visited = set()

def dfs(node):
    answer.append(str(node))
    visited.add(node)
    for neighbor in dic[node]:
        if neighbor not in visited:
            dfs(neighbor)

dfs(X)

answer2 = []

# BFS
visited = set()

def bfs(start):
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        answer2.append(str(node))
        for neighbor in dic[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfs(X)

print(" ".join(answer))
print(" ".join(answer2))