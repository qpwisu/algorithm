n = int(input())
for i in range(n):
    bracket = input()
    bl = [ bracket[i] for i in range(len(bracket))]
    open = 0
    close = 0
    asw = ""
    for j in range(len(bl)):
        b = bl.pop()
        if b == ")":
            close += 1
        else:
            open+=1
        if open > close:
            asw = "NO"
            break
    if asw =="":
        asw = "YES"

    if open != close:
        asw = "NO"
        print(asw)
        continue
    else:
        asw = "Yes"
        print(asw)
        continue
