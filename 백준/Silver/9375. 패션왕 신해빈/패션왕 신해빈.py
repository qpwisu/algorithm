from collections import defaultdict
n = int(input())

for _ in range(n):
    m = int(input())
    dic = defaultdict(set)
    for i in range(m):
        a, b = list(map(str, input().split()))
        dic[b].add(a)

    # 옷 종류
    length = len(dic.keys())

    count_li = [len(v) for v in dic.values()]
    answer = 1
    for c in count_li:
        answer = answer * (c+1)

    print(answer -1 )