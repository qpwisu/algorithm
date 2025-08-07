"""
4 7
6 13
4 8
3 6
5 12

K 무게 내에서 최대의 가치
dp[무게] = 가치
"""
n, k = map(int, input().split())  # 물건 수, 배낭 용량
items = [tuple(map(int, input().split())) for _ in range(n)]  # (무게, 가치)

dp = [0] * (k + 1)

for weight, value in items:
    new_dp = dp[:]  # 복사! 현재 상태 기준으로만 갱신
    for w in range(k + 1):
        if w + weight <= k:
            new_dp[w + weight] = max(new_dp[w + weight], dp[w] + value)
    dp = new_dp
print(max(dp))
