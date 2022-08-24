import sys
sys.stdin=open('input.txt')
T=int(input())

def MIRO(r,c):
    di = [0, 1, 0, -1] #우 하 좌 상
    dj = [1, 0, -1, 0] # r= i 쪽 c= j쪽
    global h
    h=h%4
    print(h)
    # MIRO[r+di][c+dj]
    r,c=r+di[h],c+dj[h] # 한칸 전진 (오른쪽)
    if M[r][c]==3:
        return 1
    else:
        if r>N-1 or c>N-1 or r<0 or c<0 or M[r][c]==1:
            r,c=r-di[h],c-dj[h]
            h+=1
            MIRO(r,c)
        else:                          
            M[r][c] = 1
            MIRO(r,c)

for tc in range(1,T+1):
    N=int(input())
    M=[list(map(int,input())) for _ in range(N)]
    i_d=0
    j_d=0
    for i in range(N):
        for j in range(N):
            if M[i][j]==2:
                i_d,j_d=i,j
    print(i_d,j_d)
    MIRO(i_d,j_d)
    # 찾으면 return
    # 함수끝에 return fasle