def solution(numbers):
    # 숫자를 문자열로 변환
    str_numbers = list(map(str, numbers))
    
    # 정렬 기준: 두 수를 이어 붙였을 때 더 큰 값이 되도록 정렬
    str_numbers.sort(key=lambda x: x * 4, reverse=True)  # 최대 1000까지 확장 가능
    
    # 모든 숫자가 0일 경우 예외 처리
    answer = ''.join(str_numbers)
    return '0' if answer[0] == '0' else answer