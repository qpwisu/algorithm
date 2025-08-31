"""
dp 둘중 하나 선택문제 
새롭게 배열을 초기화해서 제공해야함 
dp 인덱스가 a 흔적 값이 b 흔적 
"""
def solution(info, n, m):
    inf = float("inf")
    dp = [inf] *n
    # 처음에는 아무것도 않훔쳤으니 a흔적도 0 b도 0
    dp[0] = 0
    
    for a,b in info:
        new_dp = [inf] *n
        
        for i in range(n):
            if dp[i] == inf:
                continue 
            
            # b를 훔친경우 
            if dp[i] + b < m:
                if new_dp[i] > dp[i] + b: 
                    new_dp[i] = dp[i] + b
            # a를 훔친경우 
            if i+a < n:
                if new_dp[i+a] > dp[i]:
                    new_dp[i+a] =  dp[i] 
        dp = new_dp 
        
    
    answer = -1
            
    for i, ans in enumerate(dp):
        if dp[i] == inf:
            continue 
        answer = i 
        break 
    
    return answer