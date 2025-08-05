# 모든 경우의 수를 확인해야함 -> dfs 
# 필요 인자 total, level 
# 전역 변수 length
def solution(numbers, target):
    length = len(numbers)
    global answer
    answer = 0

    def dfs(total, level):
        global answer

        if level == length:
            if total == target:
                answer +=1 
            return
        
        dfs(total+numbers[level],level+1)
        dfs(total-numbers[level],level+1)
        
    dfs(0,0)
    return answer