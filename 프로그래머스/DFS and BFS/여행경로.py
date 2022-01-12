#딕션너리의 초기화 처리가 필요없는 defaultdictionary 사용하고 스택을 이용한 풀이 매우 어려웠음 
from collections import defaultdict
def solution(tickets):
    r = defaultdict(list) 
    #defaultdict로 초기값을 지정해준다 
    for i,j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()

    s = ["ICN"] #스택
    p = []
    while s:
        q = s[-1]
        if r[q] != []:#스택의 top에서 이동경로가 있는경우 스택에 맨앞 경로를 추가 
            s.append(r[q].pop(0))
        else: #도착 공항이 없는 경우만 p에 추가 
            p.append(s.pop())
    return p[::-1] #역순
  
  
