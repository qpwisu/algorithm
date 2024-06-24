'''오름차순 정렬'''
'''
거품정렬: 첫번째부터 마지막-1 인덱스까지 차례대로 다음 인덱스와 대소관계를 비교해 작으면 자리를 바꾼다. - 이걸 n-1회 반복
'''
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(0, len(li)-1-i):
            if li[j] > li[j+1]:
                li[j+1],li[j] = li[j],li[j+1]
    return li
'''
선택정렬: 첫번쨰부터 마지막 이전까지 이후 숫자 중 가장 작은 것의 위치를 바꿈 
'''
def selection_sort(li):
    for i in range(len(li)-1):
        num = li[i]
        max_index = -1
        for j in range(i+1,len(li)):
            if num > li[j]:
                num = li[j]
                max_index = j
        if max_index != -1:
            li[max_index], li[i] = li[i], li[max_index]
    return li

'''
삽입정렬: 두번째수 부터 앞에 있는 숫자들과 비교하여 넣어줌 
'''
def insertion_sort(li):
    for i in range(1,len(li)):
        num = li[i]
        for j in range(i,0,-1):
            if num < li[j-1]:
                li[j-1],li[j] = li[j],li[j-1]
    return li

'''
계수정렬: max(li) 이하의 수로 이루어 져있을때 [0]*max(li) 리스트를 만들어서 숫자를 카운팅
'''
def counting_sort(li):
    max_li = max(li)+1 # 0ㅠㅗ함
    count_li = [0]*max_li
    for num in li:
        count_li[num]+=1
    answer = []
    for i in range(len(count_li)):
        answer.extend([i]*count_li[i])
    return answer

'''
합병정렬: (분할 정복, 재귀사용) 리스트를 1/2로 나눠 1개씩 될때까지 나누고 리스트끼리 비교하며 합치기 
1. 리스트 분할 
'''
def merge_sort_devide(li):
    center = len(li)//2
    left = li[:center]
    right = li[center+1:]
    if len(left) > 1:
        return merge_sort_devide(left)

    if len(right) > 1:
        return merge_sort_devide(right)

    return



# def merge_sort(li):


li = [6,3,4,1,3,8,2,5,7]
print("정렬되지 않은 리스트: "+str(li))
print(bubble_sort(li))
print(selection_sort(li))
print(insertion_sort(li))
print(counting_sort(li))


