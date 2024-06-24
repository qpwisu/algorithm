import copy
def solution(triangle):
    answer = 0
    a=copy.deepcopy()
    
    for i in range(len(triangle)-1):
        for j in range(i+1):
            if a[i][j]+triangle[i+1][j] >a[i+1][j]:
                 a[i+1][j]=a[i][j]+triangle[i+1][j]
            if a[i][j]+triangle[i+1][j+1]> a[i+1][j+1]:
                a[i+1][j+1]=a[i][j]+triangle[i+1][j+1]
        

    return max(a[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
