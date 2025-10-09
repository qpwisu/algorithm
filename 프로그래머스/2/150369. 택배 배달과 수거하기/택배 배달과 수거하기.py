def solution(cap, n, deliveries, pickups):
    answer = 0
    d = n - 1
    p = n - 1

    while d >= 0 or p >= 0:
        # 뒤쪽의 불필요한 0 스킵
        while d >= 0 and deliveries[d] == 0:
            d -= 1
        while p >= 0 and pickups[p] == 0:
            p -= 1

        if d < 0 and p < 0:
            break

        # 이번 왕복 최장 거리
        answer += (max(d, p) + 1) * 2

        # 배달 소진
        cap_del = cap
        while d >= 0 and cap_del > 0:
            if deliveries[d] > cap_del:
                deliveries[d] -= cap_del
                cap_del = 0
            else:
                cap_del -= deliveries[d]
                deliveries[d] = 0
                d -= 1

        # 수거 소진
        cap_pick = cap
        while p >= 0 and cap_pick > 0:
            if pickups[p] > cap_pick:
                pickups[p] -= cap_pick
                cap_pick = 0
            else:
                cap_pick -= pickups[p]
                pickups[p] = 0
                p -= 1

    return answer