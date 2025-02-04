from collections import deque 
def solution(priorities, location):
    answer = 0
    pri = [[priorities[i],i]for i in range(len(priorities))]
    dq = deque(pri)
    n = 0 
    while len(dq) >1:
        tmp = dq.popleft()
        if max(dq)[0] > tmp[0]:
            dq.append(tmp)
        else:
            n+=1
            if tmp[1] == location:
                return n 
    return len(priorities) 