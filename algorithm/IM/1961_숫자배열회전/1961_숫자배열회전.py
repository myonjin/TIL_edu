import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]          #7 4 1
    arr_90=[[0]*n for _ in range(n)]                                #8 5 2
    arr_180 = [[0] * n for _ in range(n)]                           #9 6 3
    arr_270 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr_90[j][n-i-1]=arr[i][j]
    for i in range(n):
        for j in range(n):
            arr_180[j][n-i-1]=arr_90[i][j]
    for i in range(n):
        for j in range(n):
            arr_270[j][n-i-1]=arr_180[i][j]
    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            print(arr_90[i][j],end='')
        print(' ',end='')
        for j in range(n):
            print(arr_180[i][j],end='')
        print(' ', end='')
        for j in range(n):
            print(arr_270[i][j],end='')
        print(' ', end='')
        print()

