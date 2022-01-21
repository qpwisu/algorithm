import re

def solution(new_id):
    one=new_id.lower()
    two = re.sub("[^\w\.\-\_]","",one) #\w 모든 문자와 숫자를 뜻하고 .-_앞에 \를 붙힘으로써 모든문자,숫자,-_.를 제외(^)한갈 삭제
    three= re.sub("\.+",".",two) #.이 1회 이상있는것들을 .으로 치환
    four = re.sub("^\.|\.$","",three) # # []안이 아닌 밖에있는 ^은 맨앞의 문자를 가리킴 맨끝은 $
    if len(four)==0:
        four ="a"
    if len(four)>=16:
        four = four[:15]   
        four = re.sub("^\.|\.$","",four)
    if len(four)<=2:
        while(len(four)!=3):
            four+=four[-1]
    print(four)
    return four
