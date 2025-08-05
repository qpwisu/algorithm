L, C = map(int, input().split())
alphabet = sorted(input().split())
visited = [0] * C
res = []

def dfs(depth, idx):
    if depth == L:
        v = sum(1 for ch in res if ch in 'aeiou')
        c = L - v
        if v >= 1 and c >= 2:
            print(''.join(res))
        return
    for i in range(idx, C):
        if not visited[i]:
            visited[i] = 1
            res.append(alphabet[i])
            dfs(depth + 1, i + 1)
            visited[i] = 0
            res.pop()

dfs(0, 0)