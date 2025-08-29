"""
dp 인덱스가 인덱스 값은 만들어지는 값
"""
def solution(elements):
    n = len(elements)
    answer = 0 
    dp = elements[:]
    tmp = set()
    tmp.update(dp)
    
    for i in range(1,n):
        new_dp = dp[:]

        for j in range(n):
            idx = j +i 
            
            if idx >= n: 
                idx = j+i-n 
                
            new_dp[j] = dp[j] + elements[idx]
        tmp.update(new_dp)
        dp = new_dp
    
    answer = len(tmp)
        
    return answer