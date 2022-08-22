from pprint import pprint
import sys
sys.stdin = open('input.txt')

def DFS(start):
    visited[start] = 1
    print(start, visited)

    for next in range(1, V+1):
        if G[start][next] == 1 and visited[next] == 0:
            DFS(next)



V, E = map(int, input().split())
data = list(map(int, input().split()))
print(V, E)
print(data)

visited = [0] * (V+1)

G = [[0 for _ in range(E)] for _ in range(E)]
# pprint(G)

for i in range(E):
    '''
    G[1][2] = 1
    G[2][1] = 1

    G[data[0]][data[1]] = 1
    G[data[1]][data[0]] = 1

    G[data[2]][data[3]] = 1
    G[data[3]][data[2]] = 1
    '''
    # 0 2 4 6 8 10
    # 1 3 5 7 9 11
    G[data[i * 2]][data[i * 2 + 1]] = 1
    G[data[i * 2 + 1]][data[i * 2]] = 1
pprint(G)
DFS(1)