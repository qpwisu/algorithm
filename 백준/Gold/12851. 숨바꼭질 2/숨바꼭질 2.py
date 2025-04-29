from collections import deque

N, K = map(int, input().split())

queue = deque()
queue.append((N, 0))
visited = [0] * 100001  # 좌표가 0~100000까지만 있음
visited[N] = 1

time = 0
count = 0

while queue:
    n, t = queue.popleft()

    if n == K:
        time = t
        count += 1
        continue

    for next_n in (n * 2, n + 1, n - 1):
        if 0 <= next_n <= 100000:
            if visited[next_n] == 0 or visited[next_n] == t + 1:
                visited[next_n] = t + 1
                queue.append((next_n, t + 1))

print(time)
print(count)