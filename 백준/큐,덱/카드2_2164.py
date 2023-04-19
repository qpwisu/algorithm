from collections import deque
n = int(input())
li = [i+1 for i in range(n)][::-1]
q = deque(li)
while True:
    q.pop()
    if len(q) == 1:
        print(q[0])
        break
    tmp = q.pop()
    q.appendleft(tmp)

