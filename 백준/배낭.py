N, K = list(map(int,input().split()))
pack  = []
for _ in range(N):
    pack.append(list(map(int,input().split())))


b = [0] * (K+1)

for w,v in pack:
    for i in range(K,w-1,-1):
        b[i] = max(b[i],b[i-w]+v)
        # 현재 항목의 칼로리를 제외한 나머지 칼로리에 대해 이전에 계산된 최대 점수

print(b)