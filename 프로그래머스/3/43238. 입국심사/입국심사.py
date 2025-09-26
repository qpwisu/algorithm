# 시간을 기준으로 이분탐색, 해당 시간에 각 심사대가 처리할수 있는 인원 구하기 
# 그 인원수가 n명 이상이면 right = mid - 1 n명 이하면 left = mid +1
def solution(n, times):
    right = max(times)* n
    left = 1
    answer = 0
    while left <= right: 
        people = 0
        mid =(left+right) //2

        for t in times:
            people += (mid//t)
            if people >= n:  # 가지치기(조기 종료)
                break

        
        if people >= n:
            right = mid - 1
            answer = mid
        elif people < n:
            left = mid +1
            
      

    
    return answer