import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,2):
    n=int(input())
    arr=[list(map(int,input())) for _ in range(n)]
    m=n//2 # 가운데 숫자
    sum=0
    sum_white=0
    for i in range(n):
        for j in range(n):
            sum+=arr[i][j]

    for i in range(m):
        for j in range(m-i):
            sum_white+=arr[i][j]+arr[i][n-j-1]+arr[n-i-1][j]+arr[n-i-1][n-j-1]
    print(sum_white)
    result=sum-sum_white

    print(f'#{tc} {result}')
