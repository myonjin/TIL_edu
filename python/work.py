from operator import truediv


num = int(input())
c="년은 평년입니다"
d="년은 윤년입니다"
a=str(num)+"년은 평년입니다"
b=str(num)+"년은 윤년입니다"
if num%4==0:
    if num%100==0:
        if num%400==0:
            print(str(b))
        else:
            print(str(a))            
    else:
        print(str(b))
else:
    print(str(a))


