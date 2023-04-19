from collections import deque
n = int(input())
li = [i+1 for i in range(n)]
q = deque(li)
while (len(q)>1):
    q.popleft()
    tmp = q.popleft()
    q.append(tmp)
print(q[0])