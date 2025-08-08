"""
8 19
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 1 0 0 0 1 0 1 1 1 1 1 0
0 0 1 0 1 0 0 1 1 0 0 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 0 0 0
0 1 1 1 1 1 0 1 0 1 0 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 0 1 1 0 0 0 1 0 0 0
0 1 0 0 0 1 0 1 0 0 0 1 0 0 0 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
"""
from collections import deque
M, N = map(int, input().split())
answer =0
node = []
maps = []
for i in range(M):
    li = list(map(int,input().split()))
    for j in range(N):
        if  li[j] == 1 :
            node.append([j,i])
    maps.append(li)

dx, dy = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]

while node:
    start = node.pop()

    if maps[start[1]][start[0]] == 2:
        continue
    answer +=1
    queue = deque()
    queue.append(start)
    maps[start[1]][start[0]] = 2

    while queue:
        now = queue.popleft()

        for i in range(8):
            mx = now[0] + dx[i]
            my = now[1] + dy[i]

            if 0<= mx < N and 0<= my < M and maps[my][mx] == 1:
                queue.append([mx, my])
                maps[my][mx] = 2

print(answer)


