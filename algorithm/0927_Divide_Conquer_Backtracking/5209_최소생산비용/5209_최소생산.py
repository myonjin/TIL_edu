import sys
sys.stdin = open('input.txt')

def f(i,k,cnt):
    global result
    if cnt > result:
        return

    if i == k:
        # for di in range(N):
        #     cnt+=arr[di][ p[di] ]
        if result>=cnt:
            result=cnt


    else:
        for j in range(i,k):
            p[i],p[j] = p[j], p[i]
            cnt+=arr[i][ p[i] ]
            f(i+1,k,cnt)
            cnt -= arr[i][p[i]]
            p[i],p[j] = p[j], p[i]

T=int(input())
for tc in range(1,T+1):
    N=int(input()) #제품수
    arr=[list(map(int,input().split())) for _ in range(N)]

    p=[i for i in range(N)]
    result=9999999
    # print(p)
    f(0,N,0)
    # print(arr)
    print(f'#{tc} {result}')