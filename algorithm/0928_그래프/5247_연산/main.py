from collections import deque
import sys
sys.stdin = open('input.txt')

def bfs(N, M): # 현재 연산한 값과 목표 값
    visited[N] = 1
    q=deque()
    q.append(N)
    while q:
        # 리스트는 시간 초과 날 것
        # 데크나 front, rear 써보기
        n = q.popleft()
        operator = [n+1, n-1, n*2, n-10]

        for i in range(4):
            if operator[i] == M:
                return visited[n]
            # M과 같지 않다면, 다음 진행
            if 0 < operator[i] <= 1000000:
                # 이전에 계산했었던 결과와 동일하다면 더이상 조사할 필요 없음
                if visited[operator[i]] == 0:
                    # 몇 번만에 연산이 되었는지 저장
                    visited[operator[i]] = visited[n] + 1
                    q.append(operator[i])

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 각 결과에 대해 +1, -1, *2, -10 모든 경우의 수를 생각
    # 최악의 경우는 문제에 주어진 0~백만
    # 가지치기 -> N이 0~백만 범위를 넘어가게 된다면 cut
    # visited를 이용해서 이미 계산된 N이라면 cut
    visited = [0] * 1000001
    print(f'#{tc} {bfs(N, M)}')