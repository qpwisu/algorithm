from collections import deque 
def solution(maps):
    m = len(maps)
    n = len(maps[0])
    queue = deque()
    queue.append([0,0,1])
    maps[0][0] = -1 
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x,y,move = queue.popleft()
        
        if x == n-1 and y == m-1:
            return move
        
        for i in range(4):
            mx = dx[i] + x
            my = dy[i] + y 
            if 0<= mx <= n-1 and  0<= my <= m-1:
                if maps[my][mx] == 1:
                    queue.append([mx,my,move+1])
                    maps[my][mx] = -1 
            
        
        
    answer = -1
    return answer