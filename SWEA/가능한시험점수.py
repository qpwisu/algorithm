T = int(input())
for t in range(T):
    N = int(input())
    score_li = list(map(int, input().split()))
    sc = set([0])  # 초기에 0을 포함하는 집합 생성
    for score in score_li:
        new_scores = set()
        for existing_score in sc:
            new_scores.add(existing_score + score)
        sc.update(new_scores)  # 기존 점수 집합에 새로운 점수 합 추가
    print(f'#{t+1} {len(sc)}')
