def re(k):
    if len(k)==1 :
        return "-"
    l = int(len(k)/3)
    a= re(k[0:l]) + " "*l + re(k[2*l:])
    return a

while True:
    try:
        n = int(input())
        n = 3 ** n
        k = "-" * n
        print(re(k))
    except:
        break