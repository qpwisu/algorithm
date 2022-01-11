# n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
# 입출력 예
# numbers	target	return
# [1, 1, 1, 1, 1]	3	5

#문제를 보고 처음 생각한 방식은 재귀를 통한 dfs 깊이 우선 탐색 방법이다 


#재귀를 통한 dfs 
def solution(numbers, target):
    num_len= len(numbers)-1
    global count
    count=0
    def dfs(t,id):
        t_plus=t+numbers[id]
        t_minus=t-numbers[id]
        if id!=num_len:
            
            dfs(t_plus,id+1)
            dfs(t_minus,id+1)
        else:
            if t_plus==target or t_minus==target:
                global count
                count+=1
    dfs(0,0)
    return count

#deque를 통한 bfs 이진트리를 생각  
from collections import deque 
def solution(numbers, target):
    answer = 0
    queue = deque()
    queue.append([numbers[0],0])
    queue.append([-numbers[0],0])
    while queue:
        num,i=queue.popleft()
        if i+1 ==len(numbers):
            if target==num : 
                answer +=1
            continue     
        queue.append([num+numbers[i+1],i+1])
        queue.append([num-numbers[i+1],i+1])
    return answer
