def fibo(x):
    if x==0:
        return 0
    elif  x<3:
        return 1
    else:
        return fibo(x-1)+fibo(x-2)
a=int(input())
print(fibo(a))
