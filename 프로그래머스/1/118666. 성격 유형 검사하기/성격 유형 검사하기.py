def solution(survey, choices):
    li = [["R","T"],["C","F"],["J","M"],["A","N"]]
    dic= {}
    
    for c in ["R","T","C","F","J","M","A","N"]:
        dic[c] = 0 
    
    # 첫번쨰 비동의 두번쨰 동의 
    N = len(survey)
    for i in range(N):
        no = survey[i][0]
        yes = survey[i][1]
        
        choice = choices[i]
        if choice == 1: # 매우 비동의 3점
            dic[no] += 3
        elif choice == 2: # 비동의
            dic[no] += 2
        elif choice == 3: # 약간 비동의
            dic[no] += 1
        elif choice == 4: # 모르겠음
            continue
        elif choice == 5: # 약간 동의
            dic[yes] += 1
        elif choice == 6: # 동의 
            dic[yes] += 2
        elif choice == 7: #매우동의
            dic[yes] += 3
    answer = ''

    for a,b in li:
        if dic[a] < dic[b]:
            answer += b
        else:
            answer += a

    return answer