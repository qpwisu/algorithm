from collections import defaultdict

def solution(genres, plays):
    dic = defaultdict(list)
    dic2= defaultdict(int)

    i = 0 
    for g,p in zip(genres,plays):
        dic[g].append([i,p])
        i+=1
        dic2[g] += p
    
    tmp = list(dic2.items())
    tmp.sort(key=lambda x : -x[1])
    answer = []
    print(dic)
    for g in tmp:
        dic[g[0]].sort(key = lambda x : -x[1])
        answer.extend([ x[0] for x in  dic[g[0]][:2]])
        
    print(answer)
    return answer