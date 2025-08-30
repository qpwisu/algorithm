def solution(board, skill):
    n = len(board) # 세로
    m = len(board[0]) # 가로 
    
    diff = [[0] * (m+1) for _ in range(n+1) ]

    for sk in skill:
        tp, r1, c1, r2, c2, degree = sk
        if tp == 1: # 공격
            degree = - degree
        diff[r1][c1] += degree
        diff[r2+1][c2+1] += degree
        diff[r1][c2+1] -= degree
        diff[r2+1][c1] -= degree 
    
    # 왼 -> 오
    for i in range(n+1):
        for j in range(1,m+1):
            diff[i][j] += diff[i][j-1]
            
    # 위 -> 아래
    for i in range(m+1):
        for j in range(1,n+1):
            diff[j][i] += diff[j-1][i]
            
            
    answer = 0
    
    # 원래 그래프에 합치기 
    for i in range(n):
        for j in range(m):
            if board[i][j] + diff[i][j] > 0 :
                answer +=1
    
    return answer