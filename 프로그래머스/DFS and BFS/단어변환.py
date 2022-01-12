#dfs 방식으로 풀어보았다(코드가 복잡함)
global anlist
anlist =[]

def dfs(begin,target,words,answer):
    wc=0
    word_list=[]
    for word in words:
        count=0
        for i in range(len(word)):
            if word[i]!=begin[i]:
                count+=1
        if count ==1:
            word_list.append(word)
    
    if target in word_list:
        answer+=1
        global anlist
        anlist.append(answer)
    else: 
        for word in word_list:
            words2= words.copy()
            words2.remove(word)
            answer+=1
            dfs(word,target,words2,answer)
    if wc==0:
        return 0
    return anlist
def solution(begin, target, words):
    answer = 0
    
    dfs(begin,target,words,answer)
    if len(anlist)==0:
        return 0
    else: 
        answer=min(anlist)
    print(anlist)
    return answer
  
  
  #bfs 방식 큐를 이용하니 훨씬 쉽게 금방 풀었다 
  
from collections import deque
def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append([begin,0])
    if target not in words:
        return 0
    length = len(target)
    while queue:
        word,count=queue.popleft()
        if word == target:
            return count
        
        for i in range(len(words)):
            wd_count=0
            for j in range(length):
                if words[i][j]==word[j]:
                    wd_count +=1 
            if wd_count==length-1:
                queue.append([words[i],count+1])
                
    return answer
