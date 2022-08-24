import sys
sys.stdin=open('input.txt')
T=int(input())

def MIRO(r,c):
    di = [-1, 1, 0, 0] # 상 하
    dj = [0, 0, -1, 1] # 좌 우
    global M
    stack=[(r,c)]
    while True:
        for i in range(4):
            if 0<=r+di[i]<N and 0<=c+dj[i]<N:
                if M[r+di[i]][c+dj[i]] == 0 and (r+di[i],c+dj[i]) not in stack:
                    stack.append((r+di[i],c+dj[i]))
                elif M[r+di[i]][c+dj[i]] == 3:
                    return 1
        if stack:
            r, c = stack.pop()
            M[r][c] = 1
        else:
            return 0


for tc in range(1,T+1):
    N=int(input())
    M=[list(map(int,input())) for _ in range(N)]
    i_d=0
    j_d=0
    stack=[]
    for i in range(N):
        for j in range(N):
            if M[i][j]==2:
                i_d,j_d=i,j
    print(f'#{tc} {MIRO(i_d,j_d)}')
    # 찾으면 return
    # 함수끝에 return fasle