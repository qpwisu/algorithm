## 핵심

- sort와 sorted 차이
    - sort는 기존의 리스트를 정렬 반환 값 x
    - sorted는 정렬된 새로운 리스트를 반환

```python
sort(li)
li2 = sorted(li)
```

- 정렬 key
    - 정렬을 key값을 통해 정렬   - 람다를 사용

```python
numbers.sort(key=lambda x: x*3, reverse=True)
# if, else 사용시 : 붙히지 안음 
numbers.sort(reverse = True, key = lambda x: x if len(x) == 4 else x *3)
```

- 문자열 정렬 주의 사항
    - 문자열을 정렬할때 999, 101010이 있으면 999와 앞에 3가지만 정렬하여 101로 정렬한다