def solution(citations):
    citations = sorted(citations)
    n= len(citations)

    for h in range(n,0,-1):
        up = len([c for c in citations if c >=h])
        down = len([c for c in citations if c <h])
        
        if up >= h and down  <= h:
            return h

    answer = 0
    return answer