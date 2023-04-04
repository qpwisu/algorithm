# 순열로 모든 경우의 수 생성
from itertools import permutations
import math


def solution(numbers):
    answer = 0

    len_numbers = len(numbers)
    numbers_li = list(numbers)
    tmp_li = []

    for i in range(1, len_numbers + 1):
        perm_n = list(permutations(numbers_li, i))

        for p in perm_n:
            tmp_li.append(int("".join(p)))

    tmp_li = list(set(tmp_li))
    tmp_li = [i for i in tmp_li if i >= 2]
    print(tmp_li)
    for n in tmp_li:
        check = True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                check = False
                continue
        if check == True:
            answer += 1
    return answer