완전 탐색을 통한 DFs 
from collections import *

max_sheep = 0

def solution(info, edges):
    graph = defaultdict(set)
    for src, dst in edges:
        graph[src].add(dst)
    print(graph)
    def dfs(node, sheep, wolf, next_nodes):
        print(next_nodes)
        global max_sheep #양의 수를 전역변수 처리하여 깊이 우선 탐색을 하며 최대 양 숫자를 구한다 
        wolf  += info[node]
        sheep += (info[node] ^ 1) #XOR로 INFO(NODE)가 0일때 1을 더해준다 

        if sheep > wolf:
            max_sheep = max(max_sheep, sheep)
            for pos in graph[node]:
                next_nodes.add(pos) 

        for n_node in next_nodes:
            dfs(n_node, sheep, wolf, next_nodes-set([n_node])) #앞으로 사용될 node에서 자기 자신은 뺸다 

    dfs(0, 0, 0, set())

    return max_sheep
