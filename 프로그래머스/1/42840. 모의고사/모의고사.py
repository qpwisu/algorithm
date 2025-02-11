import math 
def solution(answers):
    n = len(answers)
    one = ([1,2,3,4,5] * (math.ceil(n/5)))[:n]
    two = ([ 2, 1, 2, 3, 2, 4, 2, 5] * (math.ceil(n/5))) [:n]
    three = ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  * (math.ceil(n/5)))[:n]
    
    def equal(answers,li):
        count = 0 
        for i in range(len(answers)):
            if answers[i] == li[i]:
                count += 1
        return count 
    
    on = equal(answers,one)
    tw = equal(answers,two)
    th = equal(answers,three)

    li = [on,tw,th]
    m = max(li)
    answers = [i + 1 for i in range(len(li)) if li[i] == m]
    return answers