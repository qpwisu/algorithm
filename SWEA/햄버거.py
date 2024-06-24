T = int(input())
for tc in range(T):
    N, L = map(int, input().split())
    items = []
    for _ in range(N):
        score, cal = map(int, input().split())
        items.append((score, cal))

    # DP 배열 초기화
    dp = [0] * (L + 1)

    # DP를 통한 최대 점수 계산
    for score, cal in items:
        for j in range(L, cal - 1, -1):
            dp[j] = max(dp[j], dp[j - cal] + score)
            print(dp[j])


    # 결과 출력
    print(f'#{tc+1} {dp[L]}')
