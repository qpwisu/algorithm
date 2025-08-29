# 유클리드 거리 
import math 
def solution(n, w, num):
    h = math.ceil(n/w)
    graph = [[False] * w for _ in range(h) ]
    target = [-1,-1] 
    answer = 1
    count = 1
    
    for i in range(h-1,-1,-1):
        tmp = math.ceil(count/w) %2 
        
        if tmp == 1 :
            for j in range(w):
                if count > n:
                    break
                if num == count:
                    target = [i,j]
                
                if i < target[0] and j == target[1]:
                    answer += 1
                    
                count += 1 
                graph[i][j] = True 
                
            
        if tmp == 0 :
            for j in range(w-1, -1 ,-1):
                if count > n:
                    break
                
                if num == count:
                    target = [i,j]
                
                if i < target[0] and j == target[1]:
                    answer += 1
                    
                count += 1 
                graph[i][j] = True 
            
    print(graph)
    return answer