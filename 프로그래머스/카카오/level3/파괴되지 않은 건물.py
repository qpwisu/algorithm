def solution(board, skill):
    answer = 0

    #board보다 행 열이 1 더 큰 배열을 만든다 
    bo = [[0 for j in range(len(board[0])+1)] for i in range(len(board) + 1)]
    
    #skill을 누적합으로 모아서 한번에 board에 추가 
    # https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/ 다시보자 
    for i in skill:
        t, r1, c1, r2, c2, degree =i
        if t ==1:
            
            bo[r1][c1]+= -degree
            bo[r1][c2+1]+=degree
            bo[r2+1][c1]+=degree
            bo[r2+1][c2+1]+= -degree
        else:
            bo[r1][c1]+=degree
            bo[r1][c2+1]+= -degree
            bo[r2+1][c1]+= -degree
            bo[r2+1][c2+1]+=degree
            
    for i in range(0,len(bo)):
        now = 0
        for j in range(0,len(bo[0])):
            now += bo[i][j]
            bo[i][j] = now
            
    for i in range(0,len(bo[0])):
        now = 0
        for j in range(0,len(bo)):
            now += bo[j][i]
            bo[j][i] = now
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += bo[i][j]
            if board[i][j]>0:
                answer+=1

    return answer
