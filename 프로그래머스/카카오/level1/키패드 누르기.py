import math
def solution(numbers, hand):
    answer = '' 
    keypad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    left="*"
    right="#"
    for i in numbers:
        if i in [1,4,7]:
            answer+="L"
            left=i
        if i in [3,6,9]:
            answer+="R"
            right=i
        if i in [2,5,8,0]:
            for p in range(4):
                for q in range(3):
                    if keypad[p][q]==i:
                        pad= [p,q]
                    if keypad[p][q]==left:
                        le = [p,q]
                    if keypad[p][q]==right:
                        ri = [p,q]   
            dis_l=math.sqrt(abs(pad[0]-le[0])+abs(pad[1]-le[1]))
            dis_r=math.sqrt(abs(pad[0]-ri[0])+abs(pad[1]-ri[1]))
            if dis_l>dis_r: 
                answer+="R"
                right =i
            elif dis_l<dis_r:
                answer+="L"
                left =i
            else : 
                if hand=="left":
                    answer+="L"
                    left =i
                else:
                    answer+="R"
                    right =i
    
    return answer
