# 문제 풀이 
#n을 8 번 이하 사용해서 number을 만들자 이중 n의 최소값을 구하자 
# for문돌려서 N번 사용해서 만들 수 있는 수들을 저장하고 이를 재활용 dp 

def solution(N, number):
    
    li = [[],[N]] 
    
    if N == number: 
        return 1 
    
    for i in range(2,9):# N 2개를 사용
        tmp_set= set()
        tmp_set.add(int(str(N)*i))

        # 문제점 2:1,3:1 이렇게만 구하고 있음 5:1, 4:2, 3:3, 2:2:2, 3:1:2 이렇게 구해진 값도 구해야함 
        
        for left_id in range(1,i):
            right_id = i - left_id
            for l in li[left_id]:
                for r in li[right_id]:
                    tmp_set.add(l + r)
                    tmp_set.add(l - r)
                    tmp_set.add(l * r)
                    tmp_set.add(l-r)
                    if l !=0:
                        tmp_set.add(r//l)
                    if r !=0:
                        tmp_set.add(l//r)
        
        if number in tmp_set:
            return i

        li.append(list(tmp_set))
     
    return -1



# def solution(N, number):
#     list1 = [0, [N]]
#     if N == number:
#         return 1
#     for i in range(2, 9):
#         list2 = []
#         a = int(str(N) * i)
#         list2.append(a)
#         for half in range(1, i // 2 + 1):
#             for x in list1[half]:
#                 for y in list1[i - half]:
#                     list2.append(x + y)
#                     list2.append(x - y)
#                     list2.append(y - x)
#                     list2.append(x * y)
#                     if x != 0 and y != 0:
#                         list2.append(x // y)
#                         list2.append(y // x)
#         if number in list2:
#             return i
#         list1.append(list2)

#     answer = -1
#     return answer