import sys
sys.stdin = open('input.txt')
T = int(input())
def bfs(S,V,A): #출발노드, 마지막정점 , 도착정점
    visited = [0]*(V+1) #마지막 정점 + 1
    q=[]
    q.append(S)
    visited[S]=0
    while q:
        S = q.pop(0)  # 디큐
        if S == A:
            return visited[A]  # 몇번을 거쳐서 왔나
        for w in arr_j[S]:  # 인접하고 미방문 정점 w가있으면
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[S] + 1
    return 0
    pass
for tc in range(1,T+1):

     V,E = map(int, input().split()) #노드의 개수,간선의 개수
    arr_j=[[] for _ in range(V+1)]
    for _ in range(E):
        a,b= map(int, input().split())
        arr_j[a].append(b)
        arr_j[b].append(a)
    print(arr_j)
    S,A = map(int,input().split()) #출발노드, 도착노드

    print(f'#{tc} {bfs(S,V,A)}')




