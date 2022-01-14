def solution(brown, yellow):
    w=0
    v=0
    answer = [[yellow,1]]
    
    for i in range(2,int(yellow/2)+1):
        if yellow%i==0:
            answer.append([int(yellow/i),i])
    l = [2*x+2*y+4 for x,y in answer]
    
    ide= l.index(brown)
    answer =answer[ide]
    answer[0]=answer[0]+2
    answer[1]=answer[1]+2
    return answer
