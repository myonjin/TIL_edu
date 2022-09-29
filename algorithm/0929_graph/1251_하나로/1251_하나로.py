import sys
sys.stdin = open('input.txt')

def prim(r,V):
    MST = [0]*V
    MST[r] = 1
    s = 0
    for _ in range(V-1):
        u = 0
        minv = 1000000000000
        for i in range(V):
            if MST[i]==1:
                for j in range(V):
                    if adjm[i][j]>0 and MST[j]==0 and minv>adjm[i][j]:
                        u = j
                        minv = adjm[i][j]
        s += minv
        MST[u]=1
    return s
T=int(input())
for tc in range(1,1+T):
    N=int(input())              #섬 개수
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    bae=float(input())
    adjm = [[0]*(N) for _ in range(N)]
    x_y=[]
    for i in range(N):
        x_y.append([x[i],y[i]])
    # print(x_y)
    for i in range(N):
        for j in range(N):
            adjm[i][j] = ((x_y[i][0]-x_y[j][0])**2 + (x_y[i][1]-x_y[j][1])**2)*bae

    # print(adjm)

    # print(prim(0,N))
    print(f'#{tc} {int(round(prim(0,N),0))}')