from collections import defaultdict


def solution(edges):
    res = [0, 0, 0, 0]
    dic = defaultdict(lambda: [0, 0])

    for x, y in edges:
        # 준거
        dic[x][0] += 1
        # 받은거
        dic[y][1] += 1
        
    for node, item in dic.items():
        give = item[0]
        take = item[1]
        # 기준 노드찾기, 들어오는건 없고 나가는게 2개 이상임
        if give >= 2 and take == 0:
            res[0] = node
        # 8자형 :8자형 시작 노드는 나가는거 들어오는거 2개 이상임
        elif give >= 2 and take >= 2:
            res[3] += 1
        # 막대기형: 마지막 도착 노드가 받기만 함 주는건 없음
        elif give == 0 and take >= 1:
            res[2] += 1
    x = dic[res[0]][0]
    res[1] = x - res[2] - res[3]
    return res

# 생성한 정점의 번호, 도넛 모양 그래프의 수, 막대 모양 그래프의 수, 8자 모양 그래프의 수

# 시간 초과 
# from collections import defaultdict,deque
# def solution(edges):
#     answer = []
#     # 정점은 양뱡향 간선이다 
#     tmp = set([e[0] for e in edges])
#     tmp2 = set([e[1] for e in edges])
#     tmp.update(tmp2)
#     n = len(tmp)
    
#     node = -1 
#     for i in range(1,n+1):
#         count = 0 
#         count2 = 0 
#         for e in edges:
#             if e[0] == i and e[1] == i:
#                 break 
            
#             if i == e[0] :
#                 count+=1 
            
#             if i == e[1]:
#                 count2+=1 
            
#         if count >= 2 and count2 ==0 :
#             node = i 
#             break
#     # 정점 == node          
#     # 그래프 시작 노드 
#     start_node = []
#     for start,end in edges:
#         if start == node:
#             start_node.append(end)
    
#     # print(node)
#     # print(start_node)
    
#     answer = [node,0,0,0]
#     for sn in start_node:
        
#         queue = deque([sn])
#         visited = [sn] 
#         while queue:
#             q = queue.popleft()
            
#             for s,e in edges:
#                 if node == s:
#                     continue
                
#                 if (s == q or e == q): 
#                     if e not in visited:
#                         queue.append(e)
#                         visited.append(e)
#                     elif s not in visited:
#                         queue.append(s)
#                         visited.append(s)
#         # print(visited)
        
#         edge_count = 0 
#         for start,end in edges:
#             if node == start:
#                 continue
                
#             if start in visited:
#                 edge_count+=1 
#                 continue
#             elif end in visited:
#                 edge_count+=1 
#                 continue
                
#         c = len(visited)
        
#         # print(c,edge_count)
#         if c == edge_count:
#             answer[1] +=1 
#         elif c==edge_count+1:
#             answer[2] +=1 
#         elif c == edge_count-1:
#             answer[3] +=1 

#     # print(answer)
#     return answer