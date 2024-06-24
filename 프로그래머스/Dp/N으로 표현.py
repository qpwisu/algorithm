def solution(N, number):
    dp_list = [0, [N]]
    answer = 0

    if N == number:
        return 1
    for i in range(2, 9):
        li = []
        li.append(int(str(N)*i))
        for j in range(1, i):
            for a in dp_list[j]:
                for b in dp_list[i - j]:
                    li.append(a + b)
                    li.append(a - b)
                    li.append(a * b)
                    if b != 0:
                        li.append(a // b)
        dp_list.append(li)
        if number in li:
            return i
    return -1

solution(5,12)

def solution(N, number):
    list1= [0,[N]]
    if N==number:
        return 1
    for i in range(2,9):
        list2 = []
        a= int(str(N)*i)
        list2.append(a)
        for half in range(1,i//2+1):
            for x in list1[half]:
                for y in list1[i-half]:
                    list2.append(x+y)
                    list2.append(x-y)
                    list2.append(y-x)
                    list2.append(x*y)
                    if x!=0 and y!=0:    
                        list2.append(x//y)
                        list2.append(y//x)
        if number in list2:
            return i
        list1.append(list2)
            
    answer = -1
    return 
