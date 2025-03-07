from collections import deque
def solution(tickets):
    answer = ["ICN"]
    n = len(tickets) 
    
    tickets.sort()
    queue = deque([("ICN",[],0)]) #시작 공항, visited, 이동 횟수 
    visited = []
    
    while queue:
        start, visit, count = queue.popleft()
        
        if count == n:
            visited = visit
            break
            
        for i in range(n):
            if i in visit:
                continue 
            
            if start == tickets[i][0]:
                queue.append((tickets[i][1],visit+[i],count+1))
        

    for i in range(n):
        answer.append(tickets[visited[i]][1])

    return answer