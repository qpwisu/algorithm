
def solution(tickets):
    li = []
    N = len(tickets)

    def  dfs(t, visited):
        visited = visited +[t]
        if N == len(visited):
            li.append(visited)
            return 
        
        start= tickets[t][0]
        end = tickets[t][1]
        
        for t in range(len(tickets)):
            if t in visited:
                continue
            if end == tickets[t][0]:
                dfs(t,visited)
        
    for t in range(len(tickets)):
        if tickets[t][0] == 'ICN':
            dfs(t,[])
    answer = []
    for l in li:
        if N+1 == len(l):
            continue
        tmp = ["ICN"]
        for t in range(len(l)):
            tmp.append(tickets[l[t]][1])
        answer.append(tmp)
        
    answer = sorted(answer)
    answer=answer[0]
    return answer
















# from collections import defaultdict
# def solution(tickets):
#     r = defaultdict(list) 
#     #defaultdict로 초기값을 지정해준다 
#     for i,j in tickets:
#         r[i].append(j)
#     for i in r.keys():
#         r[i].sort()

#     s = ["ICN"] #스택
#     p = []
#     while s:
#         q = s[-1]
#         if r[q] != []:#스택의 top에서 이동경로가 있는경우 스택에 맨앞 경로를 추가 
#             s.append(r[q].pop(0))
#         else: #도착 공항이 없는 경우만 p에 추가 
#             p.append(s.pop())
#     return p[::-1] #역순