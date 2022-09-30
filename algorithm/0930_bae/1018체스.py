N, M = map(int,input().split())
arr=[input() for _ in range(N)]     # M 가로 N 세로
min_count=99999
white='WBWBWBWB'
black='BWBWBWBW'
for i in range(M-7):
    for j in range(N-7):
        cnt=0
        for a in range(8):
            if a in [0,2,4,6]:
                for m in range(8):
                    if arr[a+j][i+0:i+8][m] != white[m]:
                        cnt+=1
            else:
                for m in range(8):
                    if arr[a+j][i+0:i+8][m] != black[m]:
                        cnt+=1
        if min_count>cnt:
            min_count=cnt

        cnt=0
        for a in range(8):
            if a in [0,2,4,6]:
                for m in range(8):
                    if arr[a+j][i+0:i+8][m] != black[m]:
                        cnt+=1
            else:
                for m in range(8):
                    if arr[a+j][i+0:i+8][m] != white[m]:
                        cnt+=1
        if min_count>cnt:
            min_count=cnt
print(min_count)