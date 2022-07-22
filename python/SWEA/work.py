

num = int(input())

a=str(num)+"년은 평년입니다"
b=str(num)+"년은 윤년입니다"
if num%4==0:
    if num%100==0:
        if num%400==0:
            print(b)
        else:
            print(a)            
    else:
        print(b)
else:
    print(a)


