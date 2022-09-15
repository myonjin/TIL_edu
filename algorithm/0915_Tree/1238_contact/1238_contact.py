from collections import deque
import sys
sys.stdin = open('input.txt')
def bfs(start):
    global result
    que=deque([start])
    visited[start]=1
    while que:
        t=que.popleft()
        for i in node[t]:
            if visited[i]==0:
                que.append(i)
                visited[i]=visited[t]+1

for tc in range(1,11):
    N,start=map(int,input().split())
    arr=list(map(int,input().split()))
    node=[[] for _ in range(101)]
    # print(node)
    # print(arr)
    result=0
    for i in range(0,N,2):
        node[arr[i]].append(arr[i+1])
    visited=[0]*101
    bfs(start)
    print(f'#{tc}',end=' ')
    for i in range(100,0,-1):
        if  visited[i]==max(visited):
            print(i)
            break


    # print(f'#{tc} {visited.index(max(visited))}')
