def solution(sizes):
    li = [] 
    
    max_size =0 
    for s in sizes:
        tmp = sorted(s)
        if tmp[1] > max_size:
            max_size = tmp[1]
        li.append(tmp)

    min_size = 0 
    
    for s in li:
        if s[0] > min_size:
            min_size = s[0]
    
    answer = max_size * min_size
    return answer