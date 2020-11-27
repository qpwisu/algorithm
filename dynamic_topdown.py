# 막대기 자르기
# 일단 막대기부터 잘라봅시다. 하나의 긴 막대기가 있는데 막대기 조각마다 가격이 다릅니다.
# 적절하게 잘라서 가장 가격이 높게 만들어야 합니다
import numpy as np

p = [0,1,5,8,9,10,17,17,20,24,30]   #길이당 막대의 가격
r= [-1]*len(p)  #길이 0~10까지의 막대의 최대 가격

def dyn_topdown(p,n):
    if r[n] >=0:
        return r[n]
    if n == 0:
        q=0

    else:
        q=-10
        for i in range(1,n+1):
            q= max(q,p[i]+dyn_topdown(p,n-i))

    r[n] = q

    return q

print(dyn_topdown(p,10))
print(r)