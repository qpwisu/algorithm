#deque를 이용한 풀이 
from collections import deque
def solution(priorities, location):
    li = [i for i in range(len(priorities))]
    p= list(zip(priorities,li))
    queue = deque(p)  
    k = []
    while queue:
        max_num = max(queue)
        n = queue.popleft()
        if n[0] ==max_num[0]:
            k.append(n)
        else: 
            queue.append(n)
    for i in range(len(k)):
        if k[i][1]==location:
            answer=i+1
    return answer
