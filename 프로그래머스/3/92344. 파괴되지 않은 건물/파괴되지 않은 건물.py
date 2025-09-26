def solution(board, skill):
    
    M = len(board)
    N = len(board[0])
    
    bo = [[0 for j in range(len(board[0])+2)] for i in range(len(board) + 2)]

    for s in skill:
        type, r1, c1, r2, c2, degree = s 
        attack = -1 
        
        if type == 2:
            attack *= -1
        
        bo[r1][c1] += degree*attack
        bo[r1][c2+1] += - (degree*attack)
        bo[r2+1][c1] += - (degree*attack)
        bo[r2+1][c2+1] += degree*attack

    for i in range(M):
        for j in range(N):
            bo[i][j+1] += bo[i][j] 
            
    for i in range(N):
        for j in range(M):
            bo[j+1][i] += bo[j][i] 
        
    for i in range(N):
        for j in range(M):
            board[j][i] += bo[j][i] 

        
        
    answer = 0
    for i in range(N):
        for j in range(M):
            if board[j][i] > 0 :
                answer +=1
    return answer