import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    #+로 분사할경우
    max_plus=0
    for i in range(N): #0,1
        for j in range(N):
            plus = arr[i][j]
            for m in range(1,M):
                di = [-1, 1, 0, 0]  # 상하좌우
                dj = [0, 0, -1, 1]
                for h in range(4):
                    if 0<=(i+di[h]*m)<N and 0<=(j+dj[h]*m)<N:
                        plus+=arr[i+di[h]*m][j+dj[h]*m]
            if plus>max_plus:
                max_plus=plus
    #=================================================================================
    # x 로 분사
    max_x=0
    for i in range(N): #0,1
        for j in range(N):
            x = arr[i][j]
            for m in range(1,M):
                di = [-1, 1, -1, 1]  # 대각
                dj = [-1, 1, 1, -1]
                for h in range(4):
                    if 0<=(i+di[h]*m)<N and 0<=(j+dj[h]*m)<N:
                        x+=arr[i+di[h]*m][j+dj[h]*m]
            if x>max_x:
                max_x=x
    if max_x>=max_plus:
        print(f'#{tc} {max_x}')
    elif max_x < max_plus:
        print(f'#{tc} {max_plus}')

