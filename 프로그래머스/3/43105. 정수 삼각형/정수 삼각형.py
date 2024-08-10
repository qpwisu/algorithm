def solution(triangle):
    answer = 0
    
    for i in range(len(triangle)-2,-1,-1):
        for j in range(len(triangle[i])):
            left = triangle[i][j] + triangle[i+1][j]
            right = triangle[i][j] + triangle[i+1][j+1]
            
            if left >= right:
                triangle[i][j] = left
            else:
                triangle[i][j]  = right 
    return triangle[0][0]









