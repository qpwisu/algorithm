# user가 원하는 할인율 이상이면 이모티콘을 구매하고 그 합이 금액을 넘으면 플러스 서비스를 가입
# 플러스 서비스 가입자수 최대가 우선
# 판매금액 최대가 다음 목표 

from itertools import product

def solution(users, emoticons):
    n = len(emoticons)
    p = len(users)
    li = list(product([10,20,30,40],repeat = n))
    
    # li [40,10,20,30] 할인율 조합
    # 각 할인율 조합에서 플러스 가입 고객수와 이모티콘 매출 값 구해야해  
    max_money = 0
    max_plus = 0 
    
    for l in li:
        # l [40,10,20,30] 
        
        sale_price = [(100 -l[i]) *  emoticons[i] /100 for i in range(n)]
        total_money = 0
        total_plus = 0 
        
        for j in range(p):
            tmp = [sale_price[s] for s in range(n) if l[s] >= users[j][0]]  
            money = sum(tmp)
            
            if money >= users[j][1]:
                total_plus +=1 
            else:
                total_money += money
        
        if total_plus > max_plus:
            max_plus = total_plus
            max_money = total_money
            
        elif total_plus == max_plus and total_money > max_money:
            max_money = total_money
            
    
                
    answer = [max_plus,max_money]
    return answer