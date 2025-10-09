def solution(today, terms, privacies):
    # 1) 유틸: YYYY.MM.DD -> 총 일수(28일 달력)
    def to_days(s):
        y, m, d = map(int, s.split('.'))
        return ((y * 12) + (m - 1)) * 28 + d

    # 2) 오늘 일수
    today_days = to_days(today)

    # 3) 약관 딕셔너리
    term_dic = {}
    for t in terms:
        w, m = t.split()
        term_dic[w] = int(m)

    # 4) 각 개인정보의 만료일 계산: (수집일 + term*28 - 1)
    answer = []
    for i, p in enumerate(privacies, start=1):
        start, code = p.split()
        expire_days = to_days(start) + term_dic[code] * 28 - 1
        if today_days > expire_days:   # 오늘이 만료일보다 크면 파기
            answer.append(i)
    return answer