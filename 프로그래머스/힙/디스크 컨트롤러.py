#start 시점 이전에 시작된 작업에서 가장 소요시간이 적은 작업을 순서대로 작업 
#시간이 나오는 경우 +1을 계속해서 푸는 방법을 공부 
def solution(jobs):
    l=len(jobs)
    start = 0
    answer = 0
    jobs.sort(key = lambda x:x[1])
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0]<=start:
                start+=jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            if i == len(jobs)-1:
                start +=1
    
    return int(answer/l)
