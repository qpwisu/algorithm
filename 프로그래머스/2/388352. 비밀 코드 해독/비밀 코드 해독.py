from itertools import combinations
def solution(n, q, ans):
    
    li = [i for i in range(1,n+1)]
    tmp = list(combinations(li,5))
    
    for i,a in enumerate(ans):
        tmp_li = []
        
        for t in tmp:
            if comparison(q[i],t,a):
                tmp_li.append(t)
        tmp = tmp_li 
        
    answer = len(tmp)
    return answer

def comparison(a,b,num):
    count = 0
    for i in range(5):
        if a[i] in b:
            count +=1 
    
    if num == count:
        return 1 
    return 0 