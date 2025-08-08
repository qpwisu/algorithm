import heapq 
def solution(N, road, K):
    answer = 0
    
    distances = [float('inf')] * (N+1)
    
    graph = [[] for i in range(N+1)]
    
    for a,b,w in road: # 양방향 
        graph[a].append([w,b]) #[가중치,도착점]
        graph[b].append([w,a]) #[가중치,도착점]

    queue = [[0,1]]
    distances[1] = 0 
    
    while queue:
        start_weight , start = heapq.heappop(queue)
        for end_weight, end in graph[start]:
            if start_weight + end_weight <  distances[end]:
                distances[end] = start_weight + end_weight
                heapq.heappush(queue,[distances[end], end])
        
    for d in distances:
        if d == float("inf") or d >K:
            continue
        else:
            answer +=1
            
    return answer