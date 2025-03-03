
from itertools import permutations
import math 

def solution(numbers):
    li = list(numbers)
    tmp_li = [int(n) for n in numbers]
    for i in range(2,len(numbers)+1):
        tmp_li.extend([int("".join(t)) for t in list(permutations(li,i))])

    set_num = set(tmp_li)    
    answer = 0
    print(set_num)
    for n in set_num:
        if n == 0 or n==1:
            continue 

        tmp = -1
        for i in range(2,int(math.sqrt(n))+1):
            if n%i ==0:
                tmp = 0 
                break
        if tmp !=0:
            answer +=1 
    return answer