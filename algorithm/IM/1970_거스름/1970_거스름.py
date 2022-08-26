import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    arr=[0,0,0,0,0,0,0,0]
    N=int(input())
    arr[0]=N//50000
    N = N % 50000
    arr[1] = N//10000
    N = N % 10000
    arr[2] = N//5000
    N = N % 5000
    arr[3] = N//1000
    N = N % 1000
    arr[4] = N//500
    N = N % 500
    arr[5] = N//100
    N = N % 100
    arr[6] = N//50
    N = N % 50
    arr[7] = N//10
    N = N % 10

    print(f'#{tc}')
    print(*arr)
