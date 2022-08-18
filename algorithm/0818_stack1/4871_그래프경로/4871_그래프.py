import sys
from pprint import pprint
sys.stdin=open('input.txt')

def DFS(start):
    visited[start] = 1
    # print(start, visited)

    for next in range(1, V+1):
        if G[start][next] == 1 and visited[next] == 0:
            DFS(next)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    stack=[]
    result=0
    for _ in range(E):
        data = list(map(int, input().split()))
        stack.append(data)
    first, last = map(int, input().split())
    visited = [0] * (V + 1)
    G = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for i in range(E):
        G[stack[i][0]][stack[i][1]] = 1

    pprint(G)
    DFS(first)
    if visited[last]:
        result=1

    print(f'#{tc} {result}')
