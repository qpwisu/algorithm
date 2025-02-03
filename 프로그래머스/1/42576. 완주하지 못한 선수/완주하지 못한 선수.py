from collections import Counter
def solution(participant, completion):
    
    for key, value in Counter(participant + completion).items():
        if value%2 ==1 :
            return key
    return ""