def solution(schedules, timelogs, startday):
    li =[]
    
    for i in range(7):
        if startday == 6:
            startday +=1 
            continue
        elif startday == 7:
            startday = 0
            continue
        startday +=1 
        li.append(i)
        
    timelogs =  [[t[i] for i in range(7) if i in li]for t in timelogs]
    
    answer = 0
    
    for s in range(len(schedules)):
        count = 0
        
        sh = schedules[s]//100
        sm = schedules[s]%100 +10
        
        if sm >=60:
            sh +=1 
            sm = sm % 60
        
        for i in range(5):
            th = timelogs[s][i]//100
            tm = timelogs[s][i]%100 
            print(th,tm)

            if th < sh:
                count +=1
            elif th == sh:
                if tm <= sm:
                    count +=1
        if count == 5:
            answer +=1 

            
    return answer