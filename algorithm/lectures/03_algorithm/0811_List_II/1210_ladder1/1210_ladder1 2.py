import sys
sys.stdin = open('input.txt')

# 나는 좌, 우, 상만 확인 할 것이다.
# 단 위는 마지막에
dx = [0, 0, -1]
dy = [-1, 1, 0]

def ladder_search(x, y):
    # 처음 시작 위치 y 기록
    # 도착할 때 까지
    while x != 0:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1:
                arr[x][y] = 0
                # 내 현재 위치 변경
                x, y = nx, ny
    return y
    
for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 2:
                # x, y 헷갈리지 말기
                x, y = i, j
    result = ladder_search(x, y)
    print(f'#{tc} {result}')
