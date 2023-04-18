c = int(input())
def st(c):
    now = 1
    stack = []
    answer = []
    for _ in range(c):
        n = int(input())

        while now <= n:
            stack.append(now)
            answer.append("+")
            now+=1

        if stack[-1] == n:
            stack.pop()
            answer.append("-")
        else:
            print("NO")
            return
    for a in answer:
        print(a)

st(c)