def solution(new_id):
    new_id=new_id.lower()
    
    word=""
    for i in new_id:
        if i.isalnum() or i=="-" or i=="_" or i==".":
            word+=i  
    while(1):
        a=word
        word=word.replace("..",".")
        if a==word:
            break

    if len(word)==0 or word==".":
        word="a"
    if len(word)>0:
        if word[0]==".":
            word=word[1:]
        if word[-1]==".":
            word=word[:-1]
    if len(word)>15:
        word= word[:15]
    if len(word)<=2:
        while(len(word)<3):
            word+=word[-1]
    if len(word)>0:
        if word[-1]==".":
            word=word[:-1]
    print(word)
    answer=0
    return word
