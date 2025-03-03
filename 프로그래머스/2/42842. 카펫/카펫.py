def solution(brown, yellow):
    
    
    for i in range(brown,0,-1):
        b = yellow / i
        if yellow%i:
            continue
        if brown == 4 + 2*i + 2*b:
            return [i+2,b+2]
            break
    
    print(a,b)
    answer = []
    return answer