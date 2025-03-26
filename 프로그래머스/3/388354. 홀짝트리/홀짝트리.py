import sys
sys.setrecursionlimit(2_000_000)  # 재귀 깊이 제한을 매우 크게 설정 (트리 크기가 최대 40만이므로)

def solution(nodes, edges_):
    visited = [-1 for _ in range(1_000_001)]  # 노드 번호가 최대 100만이므로 미리 배열 생성, -1이면 방문 안함
    edges = [[] for _ in range(1_000_001)]   # 인접 리스트 방식의 그래프 (무방향)

    for a,b in edges_ :
        edges[a].append(b)  # 양방향 연결
        edges[b].append(a)

    def dfs(cur, prev, arr) :
        cnt = 0  # 자식 수를 셈
        for nxt in edges[cur] :
            if nxt == prev : continue  # 부모 노드는 다시 안 감 (무한 루프 방지)
            dfs(nxt, cur, arr)  # 자식 노드 DFS 호출
            cnt += 1  # 자식 수 증가

        # 노드 유형 판별 (0: 홀짝노드/짝수노드, 1: 역홀수노드/역짝수노드)
        # visited[cur] = (노드번호%2 + 자식수%2) % 2
        visited[cur] = (cur % 2 + cnt % 2) % 2
        arr[visited[cur]] += 1  # 유형별 노드 수 집계 (arr[0], arr[1])

    ans = [0,0]  # [홀짝 트리 개수, 역홀짝 트리 개수]
    for node in nodes :
        if visited[node] != -1 : continue  # 이미 방문한 트리는 스킵

        arr = [0,0]  # 현재 트리의 노드 타입 개수 저장: [0]은 홀짝 노드들, [1]은 역홀짝 노드들
        dfs(node, -1, arr)  # 해당 트리 루트 잡고 DFS 실행

        # 아래는 조건에 따라 트리 타입 판별 (케이스별 예외처리 포함)

        # 만약 트리에 딱 2개의 노드만 있고 (둘 중 하나만 타입 존재),
        # 그것이 모두 하나의 타입이면 두 트리 모두로 가능 (ex: 2개의 홀짝 노드 or 2개의 역홀짝 노드)
        if (arr[0] == 0 and arr[1] == 2) or (arr[0] == 2 and arr[1] == 0) :
            ans[0] += 1
            ans[1] += 1

        # 역홀짝 노드만 있음 → 역홀짝 트리
        elif arr[0] == 0 :
            ans[1] += 1

        # 홀짝 노드만 있음 → 홀짝 트리
        elif arr[1] == 0 :
            ans[0] += 1

        # 특별 케이스: 두 개의 홀짝 노드인데 루트 노드가 홀짝 타입이면 역홀짝 트리도 가능
        elif arr[0] == 2 and visited[node] == 0 :
            ans[1] += 1

        # 두 개의 역홀짝 노드인데 루트 노드가 역홀짝이면 홀짝 트리도 가능
        elif arr[1] == 2 and visited[node] == 1 :
            ans[0] += 1

    return ans  # [홀짝 트리 수, 역홀짝 트리 수]