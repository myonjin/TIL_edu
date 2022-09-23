import sys
sys.stdin = open('input.txt')
from pprint import pprint
from collections import deque
T = int(input())
for tc in range(1, 1+T):
    N = int(input())    # 마지막 번호 N 노드 개수 E
    node = [list(map(int, input())) for _ in range(N)]
    distance = [[9999999999] * N for _ in range(N)]
    distance[0][0]=0
    # for ar in arr:
    #     node[ar[0]][ar[1]]=ar[2]
    que=deque()
    que.append([0,0])

    while que:
        i,j=que.popleft()   # start
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 도착노드 모음들
            if 0<=i+di<N and 0<=j+dj<N:
                if distance[i+di][j+dj]>distance[i][j]+node[i+di][j+dj]:
                    distance[i+di][j+dj]=distance[i][j]+node[i+di][j+dj]
                    if i+di==N-1 and j+dj==N-1:
                        continue
                    else:
                        que.append([i+di,j+dj])


    print(f'#{tc} {distance[N-1][N-1]}')