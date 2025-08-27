#크레인으로 해당 알파벳 다제거 
# bfs 사용해서 상하좌우 돌면서 벽나오면 빼기 
from collections import deque 

def solution(storage, requests):
    N = len(storage)
    M = len(storage[0])
    li = [list(s) for s in storage]
    answer = 0
    
    def train(alpha):
        for i in range(N):
            for j in range(M):
                if li[i][j] == alpha:
                    li[i][j] = 0 
                    
    def ziga(alpha):
        ids = []
        for i in range(N):
            for j in range(M):
                if li[i][j] == alpha:
                    if i == 0 or j ==0 or i== N-1 or j == M-1:
                        ids.append([i,j])
                        continue
                    if bfs(i,j):
                        ids.append([i,j])

        for y,x in ids:
            li[y][x] = 0
            
    def bfs(y,x):
        q = deque()
        q.append([y,x])
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
        flag = False 
        visited = [[y,x]]
        while q:
            y,x = q.popleft()
            
            if y == 0 or x ==0 or y== N-1 or x == M-1:   
                
                flag = True 
                break 
                
            for i in range(4):
                mx = x + dx[i]
                my = y + dy[i]
                
                if li[my][mx] == 0 and [my,mx] not in visited:
                    q.append([my,mx])
                    visited.append([my,mx])
                
        return flag
                
    for r in requests:
        if len(r) == 1:
            ziga(r)
        else:
            train(r[0])
        

    for i in range(N):
        for j in range(M):
            if li[i][j] !=0:
                answer +=1 
    return answer