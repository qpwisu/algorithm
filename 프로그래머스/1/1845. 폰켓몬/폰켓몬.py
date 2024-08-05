def solution(nums):
    answer = 0
    set_nums = set(nums)
    print(set_nums)
    answer = len(set_nums)  
    if answer > len(nums)/2:
        answer = int(len(nums)/2)
    return answer