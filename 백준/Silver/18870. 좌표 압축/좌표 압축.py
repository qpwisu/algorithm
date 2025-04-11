N = int(input())
li = list(map(int,input().split()))
dic = { num: i for i,num in enumerate(sorted(list(set(li))))}

answer = []
for num in li:
    id = dic[num]
    answer.append(id)

print(" ".join(map(str,answer)))