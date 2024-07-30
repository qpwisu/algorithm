from collections import defaultdict
n = int(input())
m= int(input())
edge = defaultdict(list)

for _ in range(m):
    start, end = list(map(int,input().split()))
    edge[start].append(end)
    edge[end].append(start)


computers = [0] * (n+1)

def dfs(computers,id):
    computers[id] = 1
    for c in edge[id]:
        if computers[c] == 0:
            dfs(computers,c)

dfs(computers,1)
print(sum(computers[2:]))

