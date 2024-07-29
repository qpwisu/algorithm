def solution(n, lost, reserve):
    # 여분이 있는 학생이 체육복을 도난당한 경우를 처리합니다.
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    # 여분이 있는 학생들이 체육복을 빌려줍니다.
    for r in sorted(reserve_set):
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    # 체육복을 가진 학생의 수를 계산합니다.
    answer = n - len(lost_set)
    return answer
