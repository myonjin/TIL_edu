import sys
sys.stdin = open('input.txt')
def dfs(i,j,d,cnt):
    global result,dessert,si,sj
    dx = [1, 1, -1, -1]
    dy = [1, -1, -1, 1]

    if d==3 and si==i and sj==j:
        if result<cnt+1:
            result=cnt+1
        return
    if i<0 or N<=i or j<0 or N<=j:

        return

    if arr[i][j] in dessert:
        return

    if 0<=i<N and 0<=j<N:
        dessert.append(arr[i][j])
        if d==0:
            dfs(i+dx[d],j+dy[d],d,cnt+1)                      #직진
            dfs(i+dx[d+1],j+dy[d+1],d+1,cnt+1)                    #방향 꺽어어

        if d==1:
            dfs(i + dx[d], j + dy[d], d, cnt + 1)
            dfs(i + dx[d+1],j+dy[d+1],d+1,cnt+1 )
        if d==2:                                              # 오른쪽위로 안가게 만들어야함함
            if si+sj != i+j:
                dfs(i + dx[d], j + dy[d], d, cnt + 1)
            else:
                dfs(i + dx[d+1], j + dy[d+1], d+1, cnt + 1)

        if d==3:
            dfs(i + dx[d],j + dy[d] ,d ,cnt+1)                      #직진
        # di= i + dx[d]                       #방향 넣어줍니다
        # dj= j + dy[d]                       #방향 넣어줍니다
    dessert.remove(arr[i][j])


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    dessert=[]
    result=-1
    for i in range(N-2):
        for j in range(1,N-1):
            dessert = []
            si=i
            sj=j
            dfs(i,j,0,-1)
    # for i in range(N-2):
    #     for j in range(1,N-1):
    #           print(i,j)
    si=0
    sj=1
    dfs(0,1,0,-1)
    # si=0
    # sj=2
    # dessert = []
    # dfs(0,2,0,-1)
    print(f'#{tc} {result}')

