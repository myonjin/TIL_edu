import sys
sys.stdin = open(' input.txt')
def f(x,y):
    global cnt
    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if 0 <= x + di < N and 0 <= y + dj < N and arr[x + di][y + dj]-arr[x][y]==1 :
            nx= x+ di
            ny= y+ dj
            cnt+=1
            f(nx,ny)
        else:
            continue

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    result=[99999,0] # 시작방,카운트
    for i in range(N):
        for j in range(N):
            cnt=1
            f(i,j)
            if  result[1]<cnt:
                result[0],result[1] = arr[i][j],cnt
            elif result[1]==cnt:
                if result[0]>arr[i][j]:
                    result[0]=arr[i][j]
    print(f'#{tc} {result[0]} {result[1]}')