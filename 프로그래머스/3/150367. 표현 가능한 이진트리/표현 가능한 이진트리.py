def is_possible_tree(bits):
    # bits 길이가 1이면 항상 가능
    if len(bits) == 1:
        return True

    mid = len(bits) // 2
    root = bits[mid]
    left = bits[:mid]
    right = bits[mid+1:]

    # 루트가 0인데 자식 중 1이 있으면 불가능
    if root == '0' and ('1' in left + right):
        return False

    # 재귀적으로 왼쪽/오른쪽 서브트리 검사
    return is_possible_tree(left) and is_possible_tree(right)


def solution(numbers):
    answer = []
    for num in numbers:
        # 1️⃣ 2진수 변환
        b = bin(num)[2:]

        # 2️⃣ 포화이진트리 크기로 패딩 (1,3,7,15,...)
        size = 1
        while size < len(b):
            size = size * 2 + 1
        b = b.zfill(size)

        # 3️⃣ 표현 가능 여부 확인
        answer.append(1 if is_possible_tree(b) else 0)

    return answer


# 예시 실행
print(solution([42]))  # [1]
print(solution([5, 42, 63]))  # [1, 1, 0]