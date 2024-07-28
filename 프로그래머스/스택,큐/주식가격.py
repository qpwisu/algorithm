"""
문제 분석 
각 price보다 가격이 떨어질때까지 +1을 해줘야한다
하나씩 추가를하다가 이전 값보다 작은경우 pop ㅎ
"""


def solution(prices):
    #     for i in range(len(prices)-1):
    #         count = 0
    #         for j in range(i+1,len(prices)):
    #             count+=1
    #             if prices[i]>prices[j]:

    #                 break
    #         answer.append(count)
    #     answer.append(0)

    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        # 스택이 비어 있지 않고 현재 가격이 스택의 마지막 가격보다 낮으면
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    # 스택에 남아 있는 값들을 처리
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer