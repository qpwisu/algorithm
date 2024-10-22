a = int(input())
w = input()

if a == 1 :
    print(1)
    exit(0)

bc = 0
rc = 0

c = w[0]
for i in range(1,a):
    if c == w[i]:
        continue
    elif c != w[i]:
        if w[i] == 'R':
            bc +=1

        elif w[i] == 'B':
            rc +=1
        c = w[i]
if w[-1] == 'R':
    rc += 1
else:
    bc+=1

if rc <= bc:
    print(rc+1)
else:
    print(bc+1)


