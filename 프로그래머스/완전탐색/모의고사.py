def solution(answers):
    answers_size = len(answers)
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_li = [0, 0, 0]

    for i in range(answers_size):
        if answers[i] == one[i % 5]:
            answer_li[0] += 1
        if answers[i] == two[i % 8]:
            answer_li[1] += 1
        if answers[i] == three[i % 10]:
            answer_li[2] += 1
    answer = []

    max_answer = max(answer_li)

    for i in range(len(answer_li)):
        if max_answer == answer_li[i]:
            answer.append(i + 1)
    return answer