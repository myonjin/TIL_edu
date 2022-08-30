import sys
sys.stdin = open('input.txt')
def miro(i,j): # i=99 j=end
    global  result
    if i==0:
        result=j
        return 1
    else:
        if j-1<0:
            if maze[i][j+1]==1:
                maze[i][j] = 0
                miro(i, j + 1)
            else:
                miro(i-1,j)
        elif j+1>99:
            if maze[i][j-1]==1:
                maze[i][j] = 0
                miro(i, j - 1)
            else:
                miro(i-1,j)

        elif 0<=j-1 and maze[i][j-1]==1: #왼쪽
            maze[i][j]=0
            miro(i,j-1)
        elif j+1<=100 and maze[i][j+1]==1: #오른쪽
            maze[i][j]=0
            miro(i,j+1)
        else:
            miro(i-1,j)



for _ in range(1,11):
    tc=int(input())
    maze=[list(map(int,input().split())) for _ in range(100)]
    end=0
    s_i, s_j = 0, 0
    for aa in range(100):
        if maze[99][aa]==2:
            end=aa
    result=0
    miro(99,end)
    print(f'#{tc} {result}')

