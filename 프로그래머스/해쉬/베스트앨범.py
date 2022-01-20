#쟁점 2차원 리스트에서 인덱스 0이 같은 값일때 인덱스 1을 기존 내림차순의 반대로 정렬하는 방법 
#람다를 이용한 정렬 
def solution(genres, plays):
    dic= {}
    for i in range(len(genres)):
        if genres[i] not in dic :
            dic[genres[i]]=[]
            dic[genres[i]].append([plays[i],i])  
        else:
            dic[genres[i]].append([plays[i],i])
    dic2={}
    for i in dic.keys():
        dic[i].sort(reverse=True)
        dic2[i]=0
        s=0
        for x in dic[i]:
            dic2[i]+=x[0]
        
    aa=sorted(dic2.items(),key=lambda x:x[1],reverse=True)
    print(aa)
    print(dic)
    answer=[]
    for i in range(len(aa)):
        t = dic[aa[i][0]]
        t.sort(reverse=True,key=lambda x:[x[0],-x[1]]) #2차원 배열 정렬  원래는 내림차순이지만 같을때는 내림차순 
        answer.append(t[0][1])
        if len(t)>1:    
            answer.append(t[1][1])
    return answer
  
  # 정렬에 람다안에 람다 쓰는 방식 
  def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer
