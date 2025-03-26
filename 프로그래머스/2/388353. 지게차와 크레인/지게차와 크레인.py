def isOutside(storage, x, y):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    outside = False

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if storage[nx][ny] == "0":
            storage[x][y] = "0"
            outside = True
            break

    if outside:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if storage[nx][ny] == "1":
                storage[nx][ny] = "0"
                isOutside(storage, nx, ny)

def fork(storage, box):  # 지게차
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    index = []
    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] == box:
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if storage[nx][ny] == "0":
                        index.append((i, j))
                        break
    for i, j in index:
        storage[i][j] = "0"
        isOutside(storage, i, j)

def crane(storage, box):  # 크레인
    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] == box:
                storage[i][j] = "1"
                isOutside(storage, i, j)

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    # 테두리에 '0' 추가 (외부 공간 표시)
    storage = [list("0" + row + "0") for row in storage]
    storage.insert(0, list("0" * (m + 2)))
    storage.append(list("0" * (m + 2)))

    for req in requests:
        if len(req) == 1:
            fork(storage, req[0])
        else:
            crane(storage, req[0])

    # 남은 컨테이너 세기
    answer = 0
    for i in range(1, len(storage) - 1):
        for j in range(1, len(storage[0]) - 1):
            if storage[i][j] not in ["0", "1"]:
                answer += 1
    return answer