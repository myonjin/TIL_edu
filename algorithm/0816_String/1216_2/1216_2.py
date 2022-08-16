import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = int(input())
    arr = []
    for _ in range(100) :
        arr.append(input())
    m=100
    result=0
    while m > 0:
        for  i in range(100): # 가로 첫줄, 2번째줄 3번째줄
            for j in range(0,101-m):
                x=arr[i][j:m+j]
                if arr[i][j:m+j]==x[::-1]:
                    result=len(x)
                    break


            for k in range(0, 101-m):
                x_s=''
                for j in range(k,m+k):
                    x_s+=arr[j][i]
                if x_s==x_s[::-1]:
                    result=len(x_s)
                    break

        if result!=0: break;

        #세로
        #세로



        m-=1
    print(f'#{tc} {result}')



