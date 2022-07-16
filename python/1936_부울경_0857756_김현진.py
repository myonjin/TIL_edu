a,b = map(int, input().split())
#가위 =1 바위 2 보 3  1<2<3<1
#A가 이기는수 1,3 2,1 3,2 -2,1 
#B가 이기는수 3,1 1,2 2,3  2,-1
if (a-b)==1 or (a-b)==-2:
    print('A')
elif (a-b)==-2 (a-b)==1:
    print('B')
else:
    print('비겼는디요')
