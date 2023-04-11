"""
배달따로 픽업 따로 하니 time 초과뜸
음수가 될 때 까지 배달, 수거 작업 -> 작업을 할 때 마다 거리를 더하기
(음수가 된 부분에서는 이전 작업에서 남았던 상자 만큼 알아서 작업한 경우가 됨!)
"""


def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    d = 0
    p = 0

    for i in range(n):
        d += deliveries[i]
        p += pickups[i]

        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (n - i) * 2
    return answer