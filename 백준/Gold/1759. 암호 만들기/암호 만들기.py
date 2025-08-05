L, C = map(int, input().split())
li = sorted(input().split())

answer = []
aei_set = {"a", "e", "i", "o", "u"}

def dfs(node_id, path, a, b):
    if node_id == C:
        if a >= 1 and b >= 2 and len(path) == L:
            answer.append("".join(path))
        return

    node = li[node_id]

    # 안 넣기
    dfs(node_id + 1, path, a, b)

    # 넣기
    if node in aei_set:
        dfs(node_id + 1, path + [node], a + 1, b)
    else:
        dfs(node_id + 1, path + [node], a, b + 1)

dfs(0, [], 0, 0)

for p in sorted(answer):
    print(p)