from collections import deque

n, k = map(int, input().split())
MAX = 100000

parent = [-1] * (MAX + 1)
visited = [False] * (MAX + 1)

dq = deque([n])
visited[n] = True

while dq:
    now = dq.popleft()
    if now == k:
        break

    for nxt in (now - 1, now + 1, now * 2):
        if 0 <= nxt <= MAX and not visited[nxt]:
            visited[nxt] = True
            parent[nxt] = now
            dq.append(nxt)

# 경로 복원
path = []
cur = k
while cur != -1:
    path.append(cur)
    if cur == n:
        break
    cur = parent[cur]

path.reverse()  # n -> ... -> k

print(len(path) - 1)           # 이동 횟수
print(" ".join(map(str, path)))