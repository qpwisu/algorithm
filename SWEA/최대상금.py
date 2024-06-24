def bfs(li, length):
    v = set()
    for num in li:
        num_list = list(num)
        for i in range(length):
            for j in range(i + 1, length):
                num_list[i], num_list[j] = num_list[j], num_list[i]
                new_num = ''.join(num_list)
                v.add(new_num)
                num_list[i], num_list[j] = num_list[j], num_list[i]  # 다시 원상복구
    return list(v)

t = int(input())
for q in range(t):
    num, swap = input().split()
    length = len(num)
    li = [num]
    for k in range(int(swap)):
        li = bfs(li, length)
    print(f"#{q+1} {max(li)}")
