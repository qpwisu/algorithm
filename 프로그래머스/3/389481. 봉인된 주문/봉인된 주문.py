import math
def solution(n, bans):
    answer = ''
    
    # 문자 길이 구하는 함수 (남겨두되, 실사용은 줄임)
    def length(n):
        l = 0
        a = 1
        while 1:
            l += 1
            a = a * 26
            if n <= a:
                break
        return l
      
    l = length(n)  # 유지 (필수는 아님)

    # 각 자리의 ord 리스트(97~122)로 변환 - bijective 26진수
    # 예: 1->"a", 26->"z", 27->"aa"
    def ord_li(x):
        if x <= 0:
            return [97]  # 안전장치
        li = []
        while x > 0:
            x -= 1
            li.append((x % 26) + 97)
            x //= 26
        li.reverse()
        return li

    # ord 리스트 -> 문자열
    def change_str(li):
        w = ""
        for i in range(len(li)):
            w = w + chr(li[i])
        return w
    
    # 문자열 -> 순위(정수). 'a'->1, ..., 'z'->26, 'aa'->27 ...
    def to_rank(s):
        k = 0
        for ch in s:
            k = k * 26 + (ord(ch) - 96)
        return k

    # --- 금지어를 순위로 변환 후 정렬/중복제거 ---
    ban_ranks = sorted({to_rank(b) for b in bans if b})

    # --- n을 금지어만큼 밀어주는 고정점 계산 ---
    # ban_rank <= n+cnt 인 동안 cnt 증가
    cnt = 0
    i = 0
    L = len(ban_ranks)
    while i < L and ban_ranks[i] <= n + cnt:
        cnt += 1
        i += 1

    # 최종 목표 순위
    target = n + cnt

    # 최종 순위를 문자열로 변환
    li = ord_li(target)
    answer = change_str(li)
    return answer