from collections import deque

def solution(queue1, queue2):
    dq1 = deque(queue1)
    dq2 = deque(queue2)

    s1 = sum(dq1)
    s2 = sum(dq2)
    total = s1 + s2
    if total % 2:          # 총합이 홀수면 절대 같아질 수 없음
        return -1

    target = total // 2
    # 최악의 경우 이동 횟수 상한: 양쪽 원소를 거의 다 옮겨보는 정도
    limit = (len(dq1) + len(dq2)) * 3
    cnt = 0

    while cnt <= limit and s1 != target:
        if s1 > target:
            if not dq1:    # 방어코드
                return -1
            x = dq1.popleft()
            s1 -= x
            dq2.append(x)
            s2 += x
        else:
            if not dq2:
                return -1
            x = dq2.popleft()
            s2 -= x
            dq1.append(x)
            s1 += x
        cnt += 1

    return cnt if s1 == target else -1