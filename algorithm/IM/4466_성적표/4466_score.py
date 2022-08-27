import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))

    arr.sort()

    sum=0
    for i in range(1,k+1):
        sum+=arr[-i]
    print(f'#{tc} {sum}')
