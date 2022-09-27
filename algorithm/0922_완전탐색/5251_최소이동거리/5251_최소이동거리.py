import sys
sys.stdin = open('input.txt')
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())    # 마지막 번호 N 노드 개수 E
    # [s, e, w] 구간 시작 s 끝 e 거리 w
    arr = [list(map(int, input().split())) for _ in range(E)]
    distance = [0] * (N + 1)
    node = [[0] * (N + 1) for _ in range(N + 1)]
    for ar in arr:
        node[ar[0]][ar[1]]=ar[2]
    # print(node)
    que=deque([0])
    while que:
        s=que.popleft()   # start
        for e in range(1,N+1): # 도착노드 모음들
            if node[s][e] and (not distance[e] or distance[e]>distance[s]+node[s][e]):
                distance[e]=distance[s]+node[s][e]
                que.append(e)
    print(f'#{tc} {distance[N]}')