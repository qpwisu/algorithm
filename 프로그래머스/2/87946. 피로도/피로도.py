from itertools import permutations
def solution(k, dungeons):
    li = [i for i in range(len(dungeons))]
    perm = list(permutations(li,len(dungeons)))
    answer = 0 

    for p in perm:
        n = 0
        k2 = k
        for i in p:
            if k2 - dungeons[i][0] < 0:
                if n > answer:
                    answer= n
                break 
            k2 -= dungeons[i][1]
            n +=1 
        
        if n > answer:
            answer = n 
    return answer