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
            queue.pop() #pop은 heappush 처럼 가장 작은 값을 가져오진않지만 기존에 heapush로 정렬된 힙에서 가장 끝의 수는 최대값을 보장함으로 pop을 사용해도된다 
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
