from collections import defaultdict

def solution(clothes):
    dic = defaultdict(list)
    for c in clothes:
        dic[c[1]].append(c[0])
    print(dic)    
    answer = 1 
    for value in dic.values():
        answer *= len(value)+1
    answer -= 1
    return answer