#heapq 사용 하는 방법을 알아야 푼다. 리스트로 매번 정렬하면서 풀면 효율성 오류 
#heapq 작은 수 부터 자동으로 정렬하여 저장한다. 반대로 하면 우선순위가 함께든 튜플로 저장하여야 한다. 
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >=2:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first >=K:
            return answer
        heapq.heappush(scoville,first+second*2)
        answer +=1
    if scoville[0] >=K:
        return answer
    return -1

print(solution([1, 2, 3, 9, 10, 12]	,7))

# def solution(scoville, K):
#     heapq.heapify(scoville) #리스트를 heap으로 변경 근데 이걸 다른 변수로 저장하면 null이 뜬다 why?
#     answer = 0
#     while len(scoville)>=2:
#         a= heapq.heappop(scoville) #맨앞 가장 작은 수를 pop한다
#         b=heapq.heappop(scoville)
#         if a<K:
#             mix= a+(b*2)
#             heapq.heappush(scoville,mix) #heap에 mix 추가
#             answer+=1
#             if len(scoville)==1 and scoville[0]<K:
#                 return -1
#         else:
#             break
#     return answer
#















