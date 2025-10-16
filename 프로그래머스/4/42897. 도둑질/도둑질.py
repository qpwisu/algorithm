def solution(money):
    n = len(money)
    if n == 1:
        return money[0]

    def rob(line):
        # 선형 하우스 로버: 인접 집 동시 선택 불가
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]
        for v in line:
            prev2, prev1 = prev1, max(prev1, prev2 + v)
        return prev1

    # 케이스1: 첫 집 포함(=> 마지막 집 제외)
    case1 = rob(money[:-1])
    # 케이스2: 첫 집 제외(=> 마지막 집 가능)
    case2 = rob(money[1:])
    return max(case1, case2)