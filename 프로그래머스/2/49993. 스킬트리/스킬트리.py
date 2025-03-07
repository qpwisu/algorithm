from itertools  import combinations
def solution(skill, skill_trees):
    skill_li = list(skill)
    
    tmp_li = []
    
    for i in range(len(skill)):
        tmp_li.append(skill[:i+1])
    
    print(tmp_li)
    
    li = [ list(s) for s in skill_trees]
    answer = 0

    for j in range(len(li)):
        tmp = ""
        for i in range(len(li[j])):
            if li[j][i] in skill:
                tmp+=li[j][i]
        if tmp in tmp_li:
            answer +=1 
        if tmp == "":
            answer +=1 

            
    return answer