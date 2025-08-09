
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    left, right = 0, N - 1
    answer= 0
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == number:
            answer =1
            break
        elif A[mid] >= number:
            right = mid -1
        else:
            left = mid + 1

    print(answer)
