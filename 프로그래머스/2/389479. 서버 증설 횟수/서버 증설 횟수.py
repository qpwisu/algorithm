from collections import deque
def solution(players, m, k):
    answer = 0
    servers = []
    servers = deque([])
    server = 1 
    
    for i, p in enumerate(players):
        
        if servers:
            if servers[0][0] == i:
                ids, s = servers.popleft()
                server -= s 
                print("서버제거 : ",ids, server)

        
        if p >= server * m:
            p2 = p // m - server +1
            servers.append([i+k,p2])
            server += p2
            answer += p2 
            print("서버추가 : ",i,p2)

    return answer