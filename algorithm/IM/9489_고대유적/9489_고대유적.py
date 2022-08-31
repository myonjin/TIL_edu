import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    a=[list(map(int,input().split())) for _ in range(N)]
    di=[-1,1,0,0]
    dj=[0,0,-1,1]
    arr_stack=[]
    for i in range(N):
        for j in range(M):

            if a[i][j]==1:

                for h in range(4):
                    line = 1
                    c=1
                    if 0<=i+di[h]*c<N and 0<=j+dj[h]*c<M and a[i+di[h]*c][j+dj[h]*c]==1:
                        while 0<=i+di[h]*c<N and 0<=j+dj[h]*c<M and a[i+di[h]*c][j+dj[h]*c]==1:
                                c+=1
                                line+=1
                    arr_stack.append(line)
    print(f'#{tc} {max(arr_stack)}')



