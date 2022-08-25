import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr=list(map(int,input().split()))
    q=[]
    i=0
    while i<M:
        x=arr.pop(0)
        arr.append(x)
        i += 1
    print(f'#{tc} {arr[0]}')