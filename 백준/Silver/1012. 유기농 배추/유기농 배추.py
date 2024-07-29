import sys 
sys.setrecursionlimit(1000000)
T = int(input())

move_x = [1,-1,0,0]
move_y = [0,0,1,-1]
def dfs(graph,x,y):
    graph[x][y] = 2
    for i in range(4):
        mx = x + move_x[i]
        my = y + move_y[i]
        if 0<=mx<len(graph) and 0<= my < len(graph[0]):
            if graph[mx][my] == 1:
                dfs(graph,mx,my)

for t in range(T):  
    m, n, k = list(map(int, input().split()))
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        y,x= list(map(int,input().split()))
        graph[x][y] = 1

    count=0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 :
                dfs(graph,i,j)
                count+=1
    print(count)