def solution(n, times):
    left, right = 1, max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for t in times:
            total += mid // t
            if total >= n:  # 가지치기(조기 종료)
                break

        if total >= n:        # mid 시간에 n명 이상 처리 가능 → 더 줄여보기
            answer = mid
            right = mid - 1
        else:                 # 처리 불가 → 시간 늘리기
            left = mid + 1

    return answer