import sys
sys.stdin = open('input.txt')


def find_way(x, y):
    global maze
    stack = [(x,y)]
    di = [-1, 1, 0, 0]      # 상 하 좌 우
    dj = [0, 0, -1, 1]

    while True:
        for i in range(4):
            if 0 <= x + di[i] < N and 0 <= y + dj[i] < N:    # 현재 위치에서 특정 방향으로 이동이 범위를 벗어나지 않고
                if maze[x + di[i]][y + dj[i]] == '0' and (x + di[i], y + dj[i]) not in stack:   # 그곳으로 이동이 가능하며 가본적 없으면
                    stack.append((x + di[i], y + dj[i]))     # 스택에 다음 위치 추가
                elif maze[x + di[i]][y + dj[i]] == '3':    # 그곳으로 이동이 가능하며 그곳이 도착지점이라면 1 리턴하고 끝
                    return 1

        if stack:     # 스택이 비어있지 않다면
            x, y = stack.pop()  # 제일 마지막으로 저장된 위치 꺼내와서 그곳으로 이동
            maze[x][y] = 1      # 방문했다는 표시를 남김
        else:         # 아직 출구를 찾지 못했으나 스택이 비었다면
            return 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                a = i
                b = j
                break

    print(f'#{tc} {find_way(a, b)}')