"""
dfs - 백트래킹
노드, 양, 늑대, 방문노드, 방문가능한 노드 
answer을 max로 업데이트 
"""
def solution(info, edges):
    dic = {}
    n = len(info)
    answer = 1

    
    for i in range(n):
        dic[i] = []
    
    for edge in edges:
        dic[edge[0]].append(edge[1])
    
    
    
    def dfs(node, s,w, use_node, able_node):
        nonlocal answer;
        
        answer = max(answer,s)
        
        for nd in able_node:
            if nd in use_node:
                continue
                
            if info[nd] == 0: # 양일때 
                dfs(node, s+1,w, use_node + [nd], able_node + dic[nd])
                
            else: # 늑대일때 
                if s > w+1:
                    dfs(node, s,w+1, use_node + [nd], able_node + dic[nd])

            
    first = dic[0].copy()
    dfs(0,1,0,[0],first)
    
    return answer