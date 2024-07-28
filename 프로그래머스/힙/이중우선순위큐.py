from heapq import heappop,heappush
import heapq

# 힙 하나만 사용하기
def solution(operations):
    heap = []
    heapq.heapify(heap)
    while operations:
        oper = operations.pop(0)
        op = oper.split(" ")
        # 숫자 추가
        if op[0] == "I":
            heapq.heappush(heap, int(op[1]))
        # 최소값 삭제
        elif op[0] == "D" and op[1] == "-1":
            if len(heap) > 0:
                heapq.heappop(heap)

        # 최대값 삭제
        else:
            if len(heap) > 0:
                heap.remove(max(heap))
                heapq.heapify(heap)

    print(heap)

    if len(heap) == 0:
        answer = [0, 0]
    else:
        answer = [max(heap), heapq.heappop(heap)]

    return answer


# 힙 두개 사용
def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1":
            if max_heap != []:
                heappop(max_heap)
                if max_heap == [] or -max_heap[0] < min_heap[0]:
                    min_heap = []
                    max_heap = []
        elif arg == "D -1":
            if min_heap != []:
                heappop(min_heap)
                if min_heap == [] or -max_heap[0] < min_heap[0]:
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heappush(max_heap, -num)
            heappush(min_heap, num)
    if min_heap == []:
        return [0, 0]
    return [-heappop(max_heap), heappop(min_heap)]