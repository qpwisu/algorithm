def solution(n, computers):
    visited = [False] * n 


    answer = 0 

    
    for idx, computer in enumerate(computers):
        
        if not visited[idx]:
            stack = [computers[idx]]
            visited[idx] = True 
            answer +=1 
        else: continue 
        
        while stack:
            computer = stack.pop()
            for i in range(n-1,-1,-1):
                if visited[i] == True:
                    continue
                if computer[i] == 1 and i!=idx:
                    stack.append(computers[i])
                    visited[i] = True 
                    
                    
            
            
    
    return answer