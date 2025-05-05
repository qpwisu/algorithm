N, T = map(int, input().split())
li = list(map(int, input().split()))

current_sum = sum(li[:T])
mx = current_sum
mc = 1

for i in range(T, N):
    current_sum = current_sum - li[i - T] + li[i]
    if current_sum > mx:
        mx = current_sum
        mc = 1
    elif current_sum == mx:
        mc += 1

if mx == 0:
    print("SAD")
else:
    print(mx)
    print(mc)