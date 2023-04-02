import heapq
def solution(operations):
    queue=[]
    
    while operations: 
        q= operations.pop(0).split(" ")
        if q[0]=="I":
            heapq.heappush(queue,int(q[1]))
        elif q[0]=="D" and q[1]=="1":
            if len(queue)==0:
                continue
            queue.remove(max(queue))  #가장 큰수를 뽑아서 제거
            heapq.heapify(queue)
        elif q[0]=="D" and q[1]=="-1":
            if len(queue)==0:
                continue
            heapq.heappop(queue)
        print(queue)
    if len(queue)==0:
        return [0,0]
    else:
        return[max(queue),min(queue)]
    answer = []
    return answer
