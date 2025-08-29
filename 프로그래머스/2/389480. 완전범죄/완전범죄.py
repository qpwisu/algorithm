def solution(info, n, m):
    INF = 10**9
    # dp[j] = "B 흔적이 j (0 <= j < m) 일 때의 A 최소값"
    if m <= 0:  # B < m 조건상 m=0이면 불가능
        return -1

    dp = [INF] * m
    dp[0] = 0

    for a, b in info:           # a: A 흔적, b: B 흔적
        new = [INF] * m
        for j in range(m):
            if dp[j] == INF:
                continue
            # 1) 이 아이템을 A에 배정: B 그대로, A만 +a
            if dp[j] + a < new[j]:
                new[j] = dp[j] + a
            # 2) 이 아이템을 B에 배정: B는 +b, A 변화 없음 (단 B < m 유지)
            nj = j + b
            if nj < m and dp[j] < new[nj]:
                new[nj] = dp[j]
        dp = new

    # 최종: A < n 을 만족하는 것 중 A 최소값 선택
    ans = min((dp[j] for j in range(m) if dp[j] < n), default=INF)
    return ans if ans != INF else -1