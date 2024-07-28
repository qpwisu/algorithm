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
  
  # # 정렬에 람다안에 람다 쓰는 방식
# def solution1(genres, plays):
#   answer = []
#   d = {e:[] for e in set(genres)}
#   for e in zip(genres, plays, range(len(plays))):
#       d[e[0]].append([e[1] , e[2]])
#   genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#   for g in genreSort:
#       temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
#       answer += temp[:min(len(temp),2)]
#   return answer

"""
문제 분석
장르별 많이 재생된 노래 2개씩 모으기 
노래는 고유번호로 구분 

기준 
1. 많이 재생된 장르의 노래 2개 먼저 삽입 
2. 장르 내에서 많이 재생된 노래 먼저 삽입 
3. 재생 횟수 동일시 고유번호 낮은거 부터 

장르 별로 dic에 카운트

"""

from collections import defaultdict


def solution(genres, plays):
    size = len(genres)
    # dic 초기화
    #     dic = {}
    #     genres_set = set(genres)
    #     for d in genres_set:
    #         dic[d] = [0,[]]
    dic = defaultdict(lambda: [0, []])

    # dic에 총재생수,[재생수,고유번호] 넣기
    #     for i in range(size):
    #         genre = genres[i]
    #         dic[genre][0] += plays[i]
    #         dic[genre][1].append([plays[i],i])

    for id, (genre, play) in enumerate(zip(genres, plays)):
        dic[genre][0] += play
        dic[genre][1].append([play, id])

    for k, v in dic.items():
        dic[k][1] = sorted(dic[k][1], key=lambda x: (-x[0], x[1]))

    li = sorted(dic.items(), key=lambda item: -item[1][0])

    answer = []

    #     for l in li:
    #         if len(l[1][1]) > 1:
    #             answer.append(l[1][1][0][1])
    #             answer.append(l[1][1][1][1])
    #         else:
    #             answer.append(l[1][1][0][1])

    for genre, (total_plays, songs) in li:
        answer.extend([id[1] for id in songs[:2]])

    print(answer)

    return answer