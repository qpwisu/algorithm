from collections import defaultdict, deque

N, K = map(int, input().split())

dic = defaultdict(deque)
answer = 0

for i in range(N):
    name_len = len(input())
    q = dic[name_len]
    # 윈도우 밖 인덱스 제거
    while q and i - q[0] > K:
        q.popleft()
    answer += len(q)
    q.append(i)

print(answer)