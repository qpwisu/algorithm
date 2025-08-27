# startday로 토일을 인덱스 추출해서 잘라내야함 

1, 5,6 
2, 4,5
3, 3,4 
4, 2,3
5, 1,2
6, 0,1 
7, 0,6
def weekend_index(start):
    id = []

    if 1<= start <= 5:
        tmp = 6 - start
        id = [tmp, tmp+1]
    elif start == 6:
        id = [0,1]
    else:
        id = [0,6]

    return id 

def time_safe(schedule,time):
    s = str(schedule)
    h = int(s[:-2])
    m = int(s[-2:]) + 10 
    
    if m >= 60:
        h+=1 
        m -= 60 
    
    # if h == 24:
    #     h = 0 
    #     m -= 60 
    
    t = h*100 + m 
    
    if (time<= t):
        return True 
    
    return False 
    


def solution(schedules, timelogs, startday):
    answer = 0
    a= str(timelogs[0][1])
    N = len(schedules)
    weekend = weekend_index(startday) 
    print(weekend)
    
    for i in range(N):
        t = schedules[i]
        flag = True
        
        for j in range(7):
            
            if j in weekend:
                continue
            
            if (not time_safe(t,timelogs[i][j])):
                flag = False 
                break 
        
        if flag == True:
            answer += 1
        
        
            
            
    
    
    return answer