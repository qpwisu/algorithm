#datatime으로 시간을 빼고 그걸 분으로 치환  
from datetime import datetime 
import math
def solution(fees, records):
    dic={}
    for i in records:
        a= i.split(" ")
        c=a[1]
        if a[1] not in dic.keys():
            dic[a[1]]=[]
            dic[a[1]].append(a[0])
        else: 
            dic[a[1]].append(a[0])
    for key,item in dic.items():
        if len(item)%2!=0:
            dic[key].append('23:59')
    print(dic)
    

    answer = []
    s= sorted(list(dic.keys()))
    print(s)
    for key in s:
        item= dic[key]
        m=0
        for i in range(0,len(item),2):
            q=datetime.strptime(item[i],"%H:%M")
            p=datetime.strptime(item[i+1],"%H:%M")
            m+=(p-q).seconds/60
        answer.append(m)
    an=[]
    print(answer)
    for i in list(map(int,answer)):
        if i <= fees[0]:
            an.append(fees[1])
        else:
            an.append(fees[1]+math.ceil((i-fees[0])/fees[2])*fees[3])
    
    return an
    
    
#기본시간, 기본요금, 단위 시간, 단위 요금 
