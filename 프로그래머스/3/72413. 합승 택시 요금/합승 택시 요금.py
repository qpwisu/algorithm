"""
1. distances inf 리스트 세팅 
2. graph[시작점] = (도착점, 가중치) 세팅 
3. heapq 시작 (가중치0, 시작점)
"""
import heapq 
def solution(n, s, a, b, fares):
    fn = n * (n-1)/2 
    answer = 0
    graph = [[] for _ in range(n+1)]
    for c,d,f in fares:
        graph[c].append((f,d))
        graph[d].append((f,c))

        
    def dijk(sn,en):
        distances = [float("inf")] * (n+1)
        queue = [(0,sn)]     
        distances[sn] = 0 
        while queue:
            weight, start = heapq.heappop(queue)

            for w, e in graph[start]:
                if  distances[start] + w < distances[e]:
                    distances[e] = distances[start] + w 
                    heapq.heappush(queue,(distances[e], e))
                    
        return distances[en]
    
    answer = float("inf")
    for i in range(1,n+1):
        distance_s = dijk(a,i)
        distance_a = dijk(b,i)
        distance_b = dijk(s,i)
        if answer > distance_a+distance_b+distance_s:
            answer = distance_a+distance_b+distance_s


    
    return answer