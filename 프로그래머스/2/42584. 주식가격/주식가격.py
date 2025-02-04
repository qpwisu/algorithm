from collections import deque 
def solution(prices):
    n = len(prices)-1
    answer = []
    prices = [[prices[i],i]for i in range(len(prices))]

    for i in range(len(prices)-1):
        tmp = n-i
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                tmp = j-i
                break
        answer.append(tmp)
    answer.append(0)
    
    return answer