def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(9)]  # 인덱스 1~8까지 사용

    for i in range(1, 9):
        # 숫자 이어붙이기: 5, 55, 555 ...
        dp[i].add(int(str(N) * i))

        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)

        if number in dp[i]:
            return i

    return -1