import math
def solution(n, k):
    a= change(n,k)
    a=a.split("0")
    print(a)
    answer = 0
    for i in a:
        if i =="" or i =='1':
            continue
        elif p_num(int(i)) is True:
            answer+=1
            
    
    return answer

def change(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1] 
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력

def p_num(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
