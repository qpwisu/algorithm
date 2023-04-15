num  = int(input())
def facto(num):
    answer = 1
    while num > 1 :
        answer = answer * num
        num -= 1
    print(answer)
facto(num)