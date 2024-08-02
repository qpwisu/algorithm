import collections
def solution(friends, gifts):
    n = len(friends)
    dic = {}
    
    for i in range(n):
        dic[friends[i]] = i
        
    present = [[0]* n for _ in range(n)] 
    
    for g in gifts:
        li = g.split(" ")
        start = li[0]
        end = li[1]
        present[dic[start]][dic[end]] += 1
        
    indicator = {}
    
    for i in range(n):
        li = [present[j][i] for j in range(n)]
        indicator[i] = sum(present[i]) - sum(li)

    result = [0]*n
    
    for i in range(n):
        for j in range(n):
            if i==j :
                continue 
            if present[i][j] > present[j][i]:
                result[i] += 1 
            
            elif present[i][j] == present[j][i] and indicator[i] > indicator[j] :
                result[i] +=1
                
    answer = max(result)
    return answer