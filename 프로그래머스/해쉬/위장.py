def solution(clothes):
    answer = 0
    hashtable = {}
    for i in clothes:
        if i[1] not in hashtable:
            hashtable[i[1]] = [i[0]]
        else:
            hashtable[i[1]].append(i[0])

    count = 1
    print(hashtable)
    for value in hashtable.values():
        count = count * (len(value) + 1)
    return count - 1