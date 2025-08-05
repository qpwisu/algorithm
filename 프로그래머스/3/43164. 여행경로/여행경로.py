# 모든 경우의 수에서 정렬된 가장 먼저 다쓰는거 
# 전역 path, visited 사용 
# 인자 level
def solution(tickets):
    tickets.sort()
    path = ["ICN"] 
    visited = [False] * len(tickets)
    answer = []
    def dfs():
        if len(path) == len(tickets)+1 :
            answer.append(path[:])
            return
    
        for id, (start, end) in enumerate(tickets):
            if visited[id] == False:
                if path[-1] == start: 
                    path.append(end)
                    visited[id] = True 
                    dfs()
                    path.pop()                    
                    visited[id] = False 

    dfs()   
    
    return answer[0]