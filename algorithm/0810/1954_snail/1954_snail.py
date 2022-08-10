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

