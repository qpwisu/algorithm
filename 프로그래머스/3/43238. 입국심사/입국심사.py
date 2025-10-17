def solution(n, times):
    answer = 0
    right = max(times) * n 
    left = 1 
    
    while left <= right:
        mid = (right+left)//2
        count = 0 
        
        for time in times:
            count += (mid // time)
            if count > n:
                break 
        
        if count >= n:
            right = mid -1 
        else:
            left = mid +1 
        
    answer = left
        
    return answer