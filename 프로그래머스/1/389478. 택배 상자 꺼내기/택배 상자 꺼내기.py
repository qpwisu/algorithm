import math
def solution(n, w, num):
    h = math.ceil(n/w)
    li = [2*w*i+1 for i in range(1,h)] # 밑층과 위층의 합은 2*w*층수 +1 이다 이를 통해 위층의 값을 알아 낼수 있음 
    nh = math.ceil(num/w) -1
    answer = 1

    m = num
    
    for i in range(nh,h-1):
        if li[i] - num <= n:
            num = li[i] - num
            answer +=1 
            
    return answer