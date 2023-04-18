def st(bl):
    open = 0
    close = 0
    for j in range(len(bl)):
        b = bl.pop()
        if b == ")":
            close += 1
        else:
            open += 1
        if open > close:
            return "NO"
    if open == close:
        return "YES"
    else:
        return "NO"


n = int(input())

for i in range(n):
    bracket = input()
    bl = [bracket[i] for i in range(len(bracket))]
    print(st(bl))
