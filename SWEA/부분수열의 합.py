def count_subsequences_with_sum(array, K):
    n = len(array)
    count = 0
    for i in range(1, 1 << n):  # 모든 부분집합을 순회 (공집합 제외)
        sum_ = 0
        for j in range(n):
            if i & (1 << j):  # j번째 원소가 부분집합에 포함되는지 확인
                sum_ += array[j]
        if sum_ == K:  # 합이 K와 일치하는 경우
            count += 1
    return count

# 입력 예시
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    array = list(map(int, input().split()))
    result = count_subsequences_with_sum(array, K)
    print(f'#{tc} {result}')
