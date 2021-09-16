from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer =[]
    for i in course:
        fd=[]
        for food in orders:
            food= sorted(food)
            food="".join(sorted(food))
            fdlist= list(food)
            a=list(combinations(food,i))
            
            
            fd+=a
        count= Counter(fd)
        count=count.most_common()
        
        
        if len(count)==0:
            break 
        elif len(count)==1:
            if count[0][1]>=2:
                answer.append(list(count[0][0]))
        else:
            if count[0][1]>=2:
                answer.append(list(count[0][0]))
            else:
                break 
                
            for i in range(len(count)-1):
                if count[i][1]== count[i+1][1]:
                    if count[i][1]>=2:
                        answer.append(list(count[i+1][0]))
                else: 
                    break 
    aa=[]
    for i in range(len(answer)):
        ak="".join(answer[i])
        aa.append(ak)
    aa=sorted(aa)

    return aa
