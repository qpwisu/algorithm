#permutations(순열)사용 combinations(조합) 이용 X 
#JOIN활용 
from itertools import permutations
def solution(numbers):
    cbn = []
    n= list(numbers)
    cbn=list(map(int,n.copy()))
    for i in range(2,len(n)+1):
        c= list(permutations(n,i))
        for j in c:
            num=int("".join(j))
            if num not in cbn:
                cbn.append(num)
    print(cbn)
    cbn = [i for i in cbn if i>=2]
    
    answer = []
    for i in cbn:
        check =0
        for s in range(2,i-1):
        # for i in range(2,int(n**0.5) + 1): - 제곱근 보다 작은수로 나눠지는 것만 찾아도됨 시간단축 
            if i%s==0:
                check=1
                break
        if check==0:
            answer.append(i)
    answer_set = set(answer)
    answer= list(answer_set)
    return len(answer)
