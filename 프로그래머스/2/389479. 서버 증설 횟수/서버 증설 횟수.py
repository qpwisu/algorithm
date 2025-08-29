from collections import deque 
def solution(players, m, k):
    answer = 0
    n = len(players) # 총시간 
    q= deque() # 사용 중인 서버 큐 (종료시간, 서버수)
    serv = 0 # 현재 사용 중인 서버 수 
    
    for i in range(n):
        
        if q:
            if q[0][0] == i: # 사용시간 다지나면 
                t, s = q.popleft()
                serv -= s 
            
        user = players[i]
        need = int(user/m) # 필요 서버수 
        
        if need > serv:
            ads = need - serv
            q.append([i+k, ads])
            serv += ads
            answer += ads
        
    
    return answer