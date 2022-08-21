import sys
sys.stdin = open('input.txt')

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def snail(x, y, N):
    # 시작점 1
    arr[x][y] = 1
    # 증가 할 값
    cnt = 2
    # 이동할 거리
    # N = 3일때, 최초 우로 3칸 이동
    move = N
    while move != 0:
        # 델타 검색 우, 하, 좌, 상
        for i in range(4):
            # 이동 할 거리
            for j in range(move):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위를 벗어나지 않고
                # 아직 방문하지 않았다면
                if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                    arr[nx][ny] = cnt
                    x, y = nx, ny
                    cnt += 1
                # 아니라면
                else:
                    # 이동 할 거리 -1
                    move -= 1

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    snail(0, 0, N)

    print(f'#{tc}')
    for i in arr:
        print(*i)