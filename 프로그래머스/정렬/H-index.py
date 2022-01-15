#문제 푸는데 어려움을 겪었다 우선 citations안에 들어 있는 값에서만 h -index가 나올수 있을꺼라 착각을 하고 풀었다 
def solution(citations):
    citations.sort()
    l=len(citations)
    answer=[]
    for i in range(len(citations)):
        up = l-i 
        down = i+1 
        if up <= citations[i]:
            answer.append(up)
            break
        if down ==1:
            answer.append(0)
    print(answer)
    return max(answer)
