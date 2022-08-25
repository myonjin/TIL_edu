import sys
sys.stdin = open('input.txt')
T = int(input())

def bfs(i, j, N):

    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 0                                   #시작점을 0으로
    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:                             # 도착점이 3인지
            return visited[i][j] - 1                    #사이 칸의 개수라서 1 빼줘야한다

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:  # 상하좌우
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and visited[ni][nj] == 0: #경계,1아니고 0일때
                q.append((ni, nj))                    #방문할 좌표를 큐에 넣어준다
                visited[ni][nj] = visited[i][j] + 1     #방문할때마다 1,2,3 값이 올라간다
    return 0                                            #while문이 끝났지만 아무런 결과 없을때 0


for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    si = 0
    sj = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
                break

    print(f'#{tc} {bfs(si, sj, N)}') #시작점의 좌표,미로의 길이