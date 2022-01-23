#각 점수에는 0점이나 어피치보다 1발더 맞추는 경우가 들어갈 수 있다. 이들을 리스트로 만들어 product로 조합을 만들었다.
#조합중 sum이 n보다 큰 것들을 제외하고 나머지에서 어피치와 라이언의 점수를 비교하여 라이언의 점수가 더 높은 경우 중 가장 점수차가 많이 나는걸 리스트에 넣었다.
#리스트에 든 동점의 조합들을 reverse 한뒤 오름차순으로 정렬하여 가장 낮은 점수에 많이 쏜 정답을 알아냈다 
def record(info,li):
    n=0
    m=0
    for i in range(len(li)):
        if li[i]==0 and info[i]==0:
            continue
        elif li[i]<=info[i]:
            m+= 10-i
        else :
            n+= 10-i
    if m>=n:
        return -1
    return n-m

from itertools import product
def solution(n, info):
    li=[]
    for i in info:
        if i!=0:
            li.append([0,i+1])
        else:
            li.append([0,1])
    
    li=list(product(*li))
    li= list(map(list,filter(lambda x : sum(x)<=n,li)))
    answer=[]
    best=0
    for i in li:
        if record(info,i)>best:
            answer=[]
            answer.append(i)
            best=record(info,i)
        elif record(info,i)==best:
            answer.append(i)
    if len(answer)==0:
        return [-1]

    for i in answer:
        i= i.reverse()
    answer.sort(reverse=True)
    answer= answer[0]
    answer=answer[::-1]
    if sum(answer)!=n:
        answer[-1]+= n-sum(answer)
    
    return answer
