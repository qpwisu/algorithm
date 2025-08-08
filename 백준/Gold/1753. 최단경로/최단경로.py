import heapq
import sys

input = sys.stdin.readline

# 무한대를 나타내는 큰 수 정의
INF = 9999999

# 입력 처리
v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
distances = [INF] * (v + 1)

# 간선 정보 입력
for _ in range(e):
    u, v_dest, w = map(int, input().split())
    graph[u].append((v_dest, w))

# 다익스트라 알고리즘 실행
queue = [(0, k)]  # (거리, 노드)
distances[k] = 0  # 시작 정점의 거리는 0

while queue:
    current_distance, current_node = heapq.heappop(queue)

    if current_distance > distances[current_node]:
        continue

    for neighbor, weight in graph[current_node]:
        distance = current_distance + weight

        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(queue, (distance, neighbor))

# 결과 출력
for i in range(1, v + 1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])
