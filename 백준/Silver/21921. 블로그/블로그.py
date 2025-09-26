# 5 2
# 1 4 2 5 1

N,X = map(int,input().split())
li = list(map(int,input().split()))
tmp = sum(li[:X])
answer = tmp
c = 1
for i in range(N-X):
    tmp += li[i+X]-li[i]
    if tmp > answer:
        answer =tmp
        c = 1
    elif tmp == answer:
        c+=1


if answer == 0:
    print("SAD")
else:
    print(answer)
    print(c)