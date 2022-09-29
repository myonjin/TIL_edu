import sys
sys.stdin = open('input.txt')
from collections import deque
def bfs(i,j):
    v[i][j]=0
    q = deque()
    q.append([i,j])
    while q:
        x,y=q.popleft()
        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            if 0<=x+di<N and 0<=y+dj<N:
                if arr[x+di][y+dj]-arr[x][y]>=0:
                    if v[x+di][y+dj]>v[x][y]+arr[x+di][y+dj]-arr[x][y]+1:
                        v[x+di][y+dj] = v[x][y]+arr[x+di][y+dj]-arr[x][y]+1
                        q.append([x+di,y+dj])
                else:
                    if v[x+di][y+dj] > v[x][y]+1:
                        v[x+di][y+dj] = v[x][y]+1
                        q.append([x+di,y+dj])



T=int(input())
for tc in range(1,1+T):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    v=[[99999]*N for _ in range(N)]
    bfs(0,0)
    # bfs(0,0)
    # print(*v,sep='\n')
    print(f'#{tc} {v[N-1][N-1]}')