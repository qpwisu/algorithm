import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min_s = heapq.heappop(scoville)
        if min_s >= K:
            return answer 
        
        if not scoville:
            if min_s <K:
                return -1 
            break 
        min_s2 = heapq.heappop(scoville)
        heapq.heappush(scoville,min_s+min_s2*2)
        answer +=1
    return -1