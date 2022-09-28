import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(N,M,cnt):
    visited[N]=1
    q=deque()
    q.append(N)
    while q:
        t=q.popleft()
        for i in [t+1,t-1,t*2,t-10]:
            if i==M:
                return visited[t]
            if visited[i] == 0 and t>0:
                visited[i] = visited[t] + 1
                q.append(i)






T= int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    visited = [0] * 1000001

    print(bfs(N,M,0))

