#해쉬 문제 
def solution(id_list, report, k):
    dic= {}
    dic2={}
    for i in id_list:
        dic[i]=[]
        dic2[i]=[]
    for i in report:
        r=i.split(" ")
        dic[r[1]].append(r[0])
        dic2[r[0]].append(r[1])
    
    li= []
    for key,item in dic.items():
        if len(set(item))>=k:
            li.append(key)
    answer = []
    for key,item in dic2.items():
        a=0
        for j in li:
            if j in item:
                a+=1
        answer.append(a)
    return answer
