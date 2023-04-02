def solution(s):
    answer = True
    left = 0
    right = 0

    for i in s:
        if i == "(":
            left += 1
        else:
            right += 1
        if right > left:
            return False

    if left != right:
        return False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True