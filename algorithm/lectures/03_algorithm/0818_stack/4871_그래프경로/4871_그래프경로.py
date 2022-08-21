import sys
sys.stdin = open('input.txt')

def dfs(v):
    # print(v)
    visited[v] = 1

    for w in range(1, V+1):
        if data[v][w] == 1 and visited[w] == 0:
            dfs(w)


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    data = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        x, y = map(int, input().split())
        data[x][y] = 1

    S, G = map(int, input().split())

    visited = [0] * (V+1)

    dfs(S)

    print(f'#{tc} {visited[G]}')