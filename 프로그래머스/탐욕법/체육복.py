def solution(n, lost, reserve):
    a= len(lost)+1
    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            a= a-1
            continue
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            a=a-1
            continue
        else:
            n-1 
    answer = n - a
    return answer
