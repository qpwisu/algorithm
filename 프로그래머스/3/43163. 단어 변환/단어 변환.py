from collections import deque 
def solution(begin, target, words):
    answer = 0
    queue = deque([(begin,0)])
    visited = [] # 한번 방문시 다시는 방문 못하게 
    while queue:
        begin_word,count = queue.popleft()
        
        # 종료 시점 
        if begin_word == target:
            answer = count
            break 
        
        for word in words:
            if word in visited:
                continue
            same_count = 0 
            for bw, w in zip(list(begin_word),list(word)):
                if bw == w :
                    same_count+=1 
            
            # 큐에 추가 
            if same_count == len(word)-1 :
                queue.append([word,count+1])
                visited.append(word)
                    
    return answer