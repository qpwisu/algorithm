#내풀이 불필요한 코드들이 많다 
def solution(s):
    l= len(s)
    li = [i for i in s]
    t=[]
    for i in range(1,l+1):
        a=[]
        n=0
        word=""
        for j in range(len(li)):
            if i!=n: 
                word+=li[j]
                n+=1
                if n==i:
                    a.append(word)
                    n=0
                    word=""
        if word !="":
            a.append(word)
        t.append(a)
    answer=[]
    for i in t:
        string =""
        w=i[0]
        count=1
        for j in range(1,len(i)):
            if i[j]==w:
                count +=1
            else: 
                if count !=1:
                    string+=(str(count)+w)
                else:
                    string+=w
                w=i[j]
                count =1
        
        if count !=1:
            string+=(str(count)+w)
        else:
            string+=w    
        answer.append(string)
    answer= min([len(i) for i in answer])
    return answer

#다른 사람 풀이 s[i:i+x]이런 방식으로 구간을 나누는 방법을 사용하지 못하고 헷갈리게 문제를 풀었다 
def solution(s):
    answer = len(s)
    for x in range(1, int(len(s)/2)+1):
        d = 0
        comp = ''
        c = 1
        for i in range(0, len(s), x):
            temp = s[i:i+x]
            if comp == temp:
                c += 1
            elif comp != temp:
                d += len(temp)
                if c > 1:
                    d += len("{}".format(c))
                c = 1
                comp = temp
        if c > 1:
            d += len("{}".format(c))
        answer = min(answer, d)
    return answer
