def solution(dirs):
    answer = 0
    visited = set()  # 방문한 경로를 저장할 집합
    node = (0, 0)  # 현재 위치를 튜플로 저장

    move = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    for dir in dirs:
        next_node = (node[0] + move[dir][0], node[1] + move[dir][1])
        
        # 좌표가 -5 ~ 5 사이인지 확인
        if -5 <= next_node[0] <= 5 and -5 <= next_node[1] <= 5:
            path = (node, next_node)  # 방향 고려한 경로 저장
            reverse_path = (next_node, node)  # 반대 방향도 같은 길로 처리

            if path not in visited:
                visited.add(path)
                visited.add(reverse_path)  # 양방향 저장
                answer += 1

            node = next_node  # 현재 위치 갱신

    return answer