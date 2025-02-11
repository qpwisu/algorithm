import heapq 
def solution(operations):
    answer = []
    heapq.heapify(answer)

    
    
    for oper in operations:
        command, num = oper.split(" ")
        if command == "I" :
            heapq.heappush(answer,int(num))
        else:
            if answer:
                if num == "-1":
                    heapq.heappop(answer)
                else:
                    answer.remove(max(answer))
                    heapq.heapify(answer)
            else:
                continue

    
    if not answer:
        return [0,0]
    
    return [max(answer),min(answer)]