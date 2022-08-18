import sys
from pprint import pprint
sys.stdin = open('input.txt')



def DFS(start):

    visited[start]=1
    print(start,visited)




V,E= map(int, input().split())
data = list(map(int , input().split()))
print(V,E)
print(data)

G =[[0 for _ in range(E)] for _ in range(E)]

pprint(G)
