# 완전 탐색 중복 순열 사용
from itertools import product


def solution(users, emoticons):
    sale_li = list(product([10, 20, 30, 40], repeat=len(emoticons)))

    join_u = 0
    money = 0

    for li in sale_li:
        jj = 0
        mm = 0
        for user in users:

            sl, l = user
            m = 0
            b = [i for i in range(len(li)) if li[i] >= sl]
            for i in b:
                m += emoticons[i] * (100 - li[i]) / 100
            if m >= l:
                jj += 1
            else:
                mm += m

        if jj > join_u:
            join_u = jj
            money = mm

        if (jj == join_u) & (mm > money):
            money = mm

    answer = [join_u, money]
    return answer