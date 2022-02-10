//정규식 활용
import re 
from itertools import permutations
def solution(expression):
    li= re.split('[-,*,+]',expression)
    li2= set(re.sub("[0-9]","",expression))
    li3= list(li2)
    li3= list(permutations(li3,len(li3)))
    print(li3)
    li4= re.split('([-,*,+])',expression)
    answer= []
    
    for opers in (li3):
        li5= li4[:]
        for oper in opers:
            oper_index= list(filter(lambda x:li5[x]==oper,range(len(li5))))
            for i in range (len(oper_index)):
                op = oper_index.pop(0)
                
                if oper == "+":  
                    li5[op-1]=int(li5[op-1])+int(li5[op+1])
                elif oper =="-":
                    li5[op-1]=int(li5[op-1])-int(li5[op+1])
                else:
                    li5[op-1]=int(li5[op-1])*int(li5[op+1])

                li5.pop(op)
                li5.pop(op)
                print(li5)

                oper_index=list(map(lambda x:x-2,oper_index))
        answer.append(li5[0])
    
        answer= list(map(lambda x:abs(x),answer))
        k= max(answer)
    return k
