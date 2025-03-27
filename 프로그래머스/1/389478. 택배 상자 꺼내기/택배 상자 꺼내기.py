import math
def solution(n, w, num):
    h = math.ceil(n/w)
    li = []
    x = -1 
    y =  math.ceil(num/w -1)
    
    count = 0
    for i in range(h):
        tmp_li = [0 for i in range(w)]
        for j in range(w):
            if n == count :
                break 
            
            count +=1 
            tmp_li[j] = count

                
        if i%2 == 1 :
            tmp_li = tmp_li[::-1]
        li.append(tmp_li)
        if num in tmp_li:
            x = tmp_li.index(num)
            
    answer = 0
    for i in range(y,h):
        if li[i][x] !=0:
            answer +=1
    return answer