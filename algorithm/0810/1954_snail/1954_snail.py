import sys
sys.stdin = open("input.txt")
T = int(input())
# 우->하->좌->상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]
    # 초기 위치 & 회전방향 설정
    x,y = 0, 0
    h = 0
    for i in range(1,N*N+1):
        snail[x][y]=i
        x+=di[h]
        y+=dj[h]
        if x>N-1 or y>N-1 or x<0 or y<0 or snail[x][y]!=0:
            x-=di[h]
            y-=dj[h]
            h+=1
            h=h%4
            x += di[h]
            y += dj[h]
    print("#{}".format(tc))
    for row in snail:
        print(*row)
    print()
