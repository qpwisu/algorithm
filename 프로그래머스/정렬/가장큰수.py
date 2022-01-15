# 처음 방식은 순열(permutation)으로 모든 경우의 수를 구해서 정렬하여 가장 큰 수를 구하려 했다 하지만 시간초과가 걸렸다 
from itertools import permutations
def solution(numbers):
    numbers = list(map(str,numbers))
    n = list(permutations(numbers,len(numbers)))
    n= list(map(''.join,n))
    numbers = list(map(int,n))
    answer = str(sorted(numbers)[-1])
    return answer
  
#문자열을 정렬했을때 숫자는 맨앞 글자부터 차례대로 정렬하는 방법을 사용해야했다 
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    #숫자가 1000이하였음으로 문자열에 3을 곱해서 sort를 해준다 ex) 9 -> 999 이게 가장 맨앞에 있어야한다 10 -> 101010 문자열에서 sort하면 앞 3개의 문자로만 sort를함 
    return str(int(''.join(numbers)))
