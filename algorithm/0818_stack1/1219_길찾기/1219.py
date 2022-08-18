import sys
from pprint import pprint
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1
    # print(start, visited)

    for next in range(100):
        if G[start][next] == 1 and visited[next] == 0:
            DFS(next)

for tc in range(1,11):
    T, E = map(int, input().split())
    data = list(map(int, input().split()))
    visited = [0] * 100
    first, last = 0,99
    G = [[0 for _ in range(100)] for _ in range(100)]
    # print(data)
    for i in range(E):
        G[data[i * 2]][data[i * 2 + 1]] = 1


    DFS(0)


    print(f'#{tc} {visited[99]}')