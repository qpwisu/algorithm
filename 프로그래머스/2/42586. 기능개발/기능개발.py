import math
def solution(progresses, speeds):
    answer = []
    tmp = []
    for p,s in zip(progresses,speeds):
        tmp.append(math.ceil((100-p)/s))
        
    n,m = tmp[0],-1
    for p in tmp:
        if p > n:
            answer.append(m+1)
            m = 0 
            n = p
        else:
            m +=1
    answer.append(m+1)

    return answer