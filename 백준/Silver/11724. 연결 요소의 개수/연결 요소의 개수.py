import sys
from collections import deque

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])

dic = {i: [] for i in range(1, N + 1)}
idx = 2
for _ in range(M):
    a = int(data[idx])
    b = int(data[idx+1])
    dic[a].append(b)
    dic[b].append(a)
    idx += 2

visited = set()
answer = 0

def dfs_stack(start):
    stack = [start]
    visited.add(start)
    while stack:
        node = stack.pop()
        for neighbor in dic[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

for i in range(1, N + 1):
    if i not in visited:
        dfs_stack(i)
        answer += 1

print(answer)