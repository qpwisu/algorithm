def solution(m, n, puddles):
    table = [[0] * (m + 1) for i in range(n + 1)]
    table[1][1] = 1
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if i == 1 and j == 1:
                continue

            if [i, j] in puddles:
                table[j][i] = 0
            else:

                table[j][i] = table[j - 1][i] + table[j][i - 1]
    print(table)
    return table[-1][-1] % 1000000007