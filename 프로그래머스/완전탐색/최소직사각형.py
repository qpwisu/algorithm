# 큰거중에 가장 큰거 * 작은거 중에 가장 큰거
def solution(sizes):
    l_li = []
    s_li = []
    for i in sizes:
        if i[0] >= i[1]:
            l_li.append(i[0])
            s_li.append(i[1])

        else:
            l_li.append(i[1])
            s_li.append(i[0])

    answer = max(l_li) * max(s_li)

    return answer