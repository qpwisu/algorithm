def solution(s):
    answer = True
    li = list(s)
    left = 0 
    right = 0 
    while li:
        tmp = li.pop()
        if tmp == "(":
            if right == 0 :
                return False 
            elif right >0 :
                right -=1 

        elif tmp == ")":
            right +=1 
    
    if left !=0 or right !=0:
        return False

    return True