def solution(n, q, ans):
    K = 5  # 뽑을 개수(고정 5)
    # 질의들을 원소 집합으로
    q_sets = [set(s) for s in q]
    Q = len(q_sets)

    # 각 숫자(1..n)가 각 질의에 포함되는지 미리 bool 테이블로
    # in_q[i][x] = x가 i번째 질의에 포함? (i:0..Q-1, x:1..n)
    in_q = [[False]*(n+1) for _ in range(Q)]
    for i, s in enumerate(q_sets):
        for x in s:
            in_q[i][x] = True

    # rem_in_q[i][pos] = pos..n 중에서 i번째 질의에 속하는 원소 개수 (suffix sum)
    rem_in_q = [[0]*(n+2) for _ in range(Q)]
    for i in range(Q):
        for pos in range(n, 0, -1):
            rem_in_q[i][pos] = rem_in_q[i][pos+1] + (1 if in_q[i][pos] else 0)

    answer = 0
    cnt = [0]*Q  # 현재까지 각 질의와의 교집합 크기

    def dfs(pos, picked):
        nonlocal answer, cnt

        # 가지치기 0: 남은 숫자로 K개를 못 채우면 중단
        if picked + (n - pos + 1) < K:
            return

        # 가지치기 1: 각 질의별 하한/상한 체크
        # - 이미 ans[i]를 초과한 경우 불가
        # - 앞으로 최대한 더 맞아도 ans[i]에 못 미치면 불가
        for i in range(Q):
            if cnt[i] > ans[i]:   # 상한 위반
                return
            # 앞으로 선택 가능한 ‘해당 질의에 속하는’ 최대치
            #   = rem_in_q[i][pos], 하지만 실제로 뽑을 수 있는 총 남은 개수 K-picked 도 상한
            max_add = min(rem_in_q[i][pos], K - picked)
            if cnt[i] + max_add < ans[i]:  # 하한 미달
                return

        # 종료: K개 뽑으면 정답 체크(여기 오면 조건 이미 만족)
        if picked == K:
            # 위에서 하한/상한으로 모두 걸렀으므로 이 시점엔 정확히 일치
            answer += 1
            return

        if pos > n:
            return

        # 선택하지 않기
        dfs(pos+1, picked)

        # 선택하기
        for i in range(Q):
            if in_q[i][pos]:
                cnt[i] += 1
        dfs(pos+1, picked+1)
        for i in range(Q):
            if in_q[i][pos]:
                cnt[i] -= 1

    dfs(1, 0)
    return answer