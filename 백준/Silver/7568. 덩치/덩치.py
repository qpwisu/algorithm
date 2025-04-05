N = int(input())
li = [list(map(int,input().split())) + [i] for i in range(N)]
li.sort(reverse=True)

answer =[]
for i in range(N):
    w,h,z= li[i]
    tmp = 1

    for j in range(i):
        w2, h2, z2 = li[j]
        if w2 > w and h2 > h:
            tmp +=1
    answer.append([z,tmp])

answer.sort()

a = [str(answer[i][1])for i in range(N)]
a = " ".join(a)
print(a)