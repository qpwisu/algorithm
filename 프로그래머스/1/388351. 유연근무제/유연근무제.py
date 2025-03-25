
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
#16:13
def solution(schedules, timelogs, startday):
    answer = len(schedules)

    for i, time in enumerate(timelogs):
        limit=schedules[i]+10
        if limit%100>59: 
            limit+=100
            limit-=60

        day=startday
        print(limit)
        for j in time:
            print(day)

            if (day!=6 and day!=7) and j>limit:     #괄호에 or가 아니라 and
                answer-=1
                break

            day%=7     #나머지 연산
            day+=1

    return answer
# 단, 토요일, 일요일의 출근 시각은 이벤트에 영향을 끼치지 않습니다. 
#1. 각 사람마다 마지노 선 알아야 함
#2. 토, 일인 인덱스 알아야 함.