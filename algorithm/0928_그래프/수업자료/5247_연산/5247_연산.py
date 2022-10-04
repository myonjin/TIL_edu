import sys
sys.stdin = open('input.txt')

def BFS(N, M):
    visited[N] = 1
    Q = [N]
    while Q:
        n = Q.pop(0)
        operator = [n+1, n-1, n*2, n-10]

        for i in range(4):
            if operator[i] == M:
                return visited[n]
            if 0 < operator[i] <= 1000000:
                if visited[operator[i]] == 0:
                    visited[operator[i]] = visited[n] + 1
                    Q.append(operator[i])

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    print(BFS(N, M))