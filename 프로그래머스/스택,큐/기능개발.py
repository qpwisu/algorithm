# stack으로 시간을 1초씩 추가하며 풀이
def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
  
# deque로 걸리는 날짜를 일괄로 구해서 풀이 
import math
from collections import deque 
def solution(progresses, speeds):
    queue =deque()
    answer=[]
    for i in range(len(progresses)):
        queue.append(math.ceil((100-progresses[i])/speeds[i]))
    
    day =queue.popleft()
    count=1
    while queue:
        q= queue.popleft()
        if day>=q:
            count+=1 
        else: 
            answer.append(count)
            count=1
            day=q
    answer.append(count)
    print(queue)
    return answer
