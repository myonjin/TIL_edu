import sys
sys.stdin = open('input.txt')
def dfs(i, j):
    global result
    if maze[i][j] == 3: # 3번인가???
        result=1
    else:
        visited[i][j] =1
        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]: #  상 하 좌 우
            ni,nj=i+di,j+dj
            if maze[ni][nj] != 1 and visited[ni][nj] == 0: #벽이아니고 , 방문안했고
                dfs(ni,nj)
        #   if dfs(ni,nj):  재귀를 쓰려면
        #      return 1
        visited[i][j] = 0 # 여기서 포문이 다돌아가고(벽에막히면) 0대입 다시 백할수있게하기위해서
        #return 0

for _ in range(1,11):
    tc=int(input())
    maze=[list(map(int,input())) for _ in range(16)]
    # print(maze)
    sti = 0
    stj = 0
    for i in range(16):          #2인좌표 찾아준다
        for j in range(16):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
    result=0
    # print (sti,stj)
    # print(visited)
    visited=[[0]*16 for _ in range(16)]
    dfs(sti, stj)
    print(f'#{tc} {result}') #도착하면 1 , 도착못하면 0


