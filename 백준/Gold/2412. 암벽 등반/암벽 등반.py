from collections import deque

N,T = list(map(int,input().split()))
dic = { i: set() for i in range(0,T+1)}

for i in range(N):
    x,y = list(map(int,input().split()))
    dic[y].add(x)

visited = set()
visited.add((0,0))

queue = deque()
queue.append([0,0,0])
answer = -1

while queue:
    x,y,c = queue.popleft()
    if y == T:
        answer = c
        break
    for i in range(-2,3):
        for j in range(-2,3):
            if i ==0 and j ==0 :
                continue

            dx = x + i
            dy = y + j

            if 0<= dx <= 1000000 and 0<= dy <= T:
                if dx in dic[dy] and (dx,dy) not in visited:
                    queue.append([dx,dy,c+1])
                    visited.add((dx,dy))
print(answer)