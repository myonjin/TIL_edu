import sys
sys.stdin = open('input.txt')

def dfs(i,j):
    global result,min_result
    if result>=min_result:
        return 0
    elif i==N-1 and j==N-1:
        if result<=min_result:
            min_result=result
    for mi,mj in [[1,0],[0,1]]:
        di=i+mi
        dj=j+mj
        if 0<=di<N and 0<=dj<N:
            result+=arr[di][dj]
            dfs(di,dj)
            result-=arr[di][dj]

T=int(input())
for tc in range(1,T+1):
    N=int(input()) # 가로 세로
    arr=[list(map(int,input().split())) for _ in range(N)]
    min_result=99999
    result=arr[0][0]
    dfs(0,0)
    print(f'#{tc} {min_result}')

