## 핵심

- stack : 후입선출
    - List.pop()

- Queue : 선입선출
    - `List.pop(0)` - 시간복잡도 O(n) 안좋음
    - deque 사용시  추가,삭제은 O(1)이지만 접근은 O(n)임
    
    ```python
    from collections import deque
    q = deque([1,2,3])
    q.append(1)
    q.appendleft(2)
    q.popleft()
    ```
    
    - queue 사용시 추가,삭제은 O(1)이지만 접근은 불가, but 멀티스레드 사용시 내부적으로 locking 지원