## 핵심

- 힙 : **최댓값과 최솟값을 찾는 연산**을 빠르게 하기 위해 고안된 완전이진트리
- 최소 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙  - default  최소값 추출
- 최대 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙 - 최대값 추출

```python
import heapq

# 힙에 추가 
heap = []
heapq.heappush(heap, 50)
print(heap)

# 리스트를 힙으로
heap2 = [50 ,10, 20]
heapq.heapify(heap2) # 다른 변수로 저장하면 안됌 
print(heap2)

#힙 최소값 삭제 및 리턴
result = heapq.heappop(heap)

#힙 최소값 리턴 
result2 = heap[0]

# 최소힙 내 최대값 제거 
queue.remove(max(queue))
# 힙에서 pop이 아닌 제거 이후 힙 재정렬 
heapq.heapify(queue) 

#최대 힙 구현 
heap_items = [1,3,5,7,9]

max_heap = []
for item in heap_items:
  heapq.heappush(max_heap, (-item, item))

print(max_heap)

```

- [디스크 컨트롤러](https://github.com/qpwisu/algorithm/blob/master/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/%ED%9E%99/%EB%94%94%EC%8A%A4%ED%81%AC%20%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC.py)
    - start 시점 이전에 시작된 작업에서 가장 소요시간이 적은 작업을 순서대로 작업
    - 시간이 나오는 경우 +1을 계속해서 푸는 방법을 공부