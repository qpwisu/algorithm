n = int(input())
def top(n, a, b, c):
    if n == 1: # 마지막 단계 가장큰 원판을 3으로 이동
        print(a, c)
    else:
        top(n-1, a, c, b) # 1의 원판을 2로 이동을 재귀적으로 이동
        print(a, c) #
        top(n-1, b, a, c) # 2의 원판을 3으로 이동
sum = 2 ** n - 1
print(sum)

top(n, 1, 2, 3)