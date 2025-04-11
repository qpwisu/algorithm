N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
li.sort()

for l in li:
    print(f'{l[0]} {l[1]}')