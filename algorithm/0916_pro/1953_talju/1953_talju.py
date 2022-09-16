import sys
sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque
def bfs(i,j):
    que=deque([])
    que.append((i,j))
    visited[i][j]=1
    while que:

        i,j = que.popleft()
        if arr[i][j]==1:
            for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:  # 상하좌우
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                    if di==-1 and arr[ni][nj] in [1,2,5,6]:
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    elif di==1 and arr[ni][nj] in [1,2,4,7]:
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    elif dj==-1 and arr[ni][nj] in [1,3,4,5]:
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    elif dj==+1 and arr[ni][nj] in [1,3,6,7]:
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    else:
                        continue

        elif arr[i][j]==2:
            for di, dj in [[-1,0],[1,0]]:  # 상하
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                    if di==-1 and arr[ni][nj] in [1,2,5,6]:
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    elif di==1 and arr[ni][nj] in [1,2,4,7]:
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    else:
                        continue

        elif arr[i][j]==3:
            for di, dj in [[0,-1],[0,1]]:  # 좌우
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                    if dj==-1 and arr[ni][nj] in [1,3,4,5]:
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    elif dj==+1 and arr[ni][nj] in [1,3,6,7]:
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    else:
                        continue

        elif arr[i][j]==4:
            for di, dj in [[-1,0], [0, 1]]:  # 상우
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                    if di==-1 and arr[ni][nj] in [1,2,5,6]: #상
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    elif dj==+1 and arr[ni][nj] in [1,3,6,7]: #우
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    else:
                        continue


        elif arr[i][j]==5:
            for di, dj in [[1,0],[0,1]]:  # 하우
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and visited[ni][nj] == 0:

                    if di == 1 and arr[ni][nj] in [1,2, 4, 7]:  # 하
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1

                    elif dj == +1 and arr[ni][nj] in [1,3, 6, 7]:  # 우
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    else:
                        continue

        elif arr[i][j]==6:
            for di, dj in [[1,0],[0,-1]]:  # 하좌
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                    if di == 1 and arr[ni][nj] in [1,2, 4, 7]:  # 하
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    elif dj == -1 and arr[ni][nj] in [1,3, 4, 5]:  # 좌
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    else:
                        continue

        elif arr[i][j]==7:
            for di, dj in [[-1,0],[0,-1]]:  # 상좌
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                    if di == -1 and arr[ni][nj] in [1,2, 5, 6]:  # 상
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    elif dj == -1 and arr[ni][nj] in [1,3, 4, 5]:  # 좌
                        que.append((ni, nj))  # 방문할 좌표를 큐에 넣어준다
                        visited[ni][nj] = visited[i][j] + 1
                    else:
                        continue

T= int(input())
for tc in range(1,T+1):
    N,M,R,C,L=map(int,input().split()) #세로i,가로j,맨홀세로i,멘홀가로j, 탈출호 수요된 시간
    arr=[list(map(int,input().split())) for _ in range(N)]
    visited=[[0]*M for _ in range(N)]
    result=0
    bfs(R,C)
    for visited_row in visited:
        for i in range(1,L+1):
            result+=visited_row.count(i)
    print(f'#{tc} {result}')