import sys
sys.stdin = open('input_1219.txt')
def bfs(V,N): # V 시작정점, N 마지막 정점 번호
    visited = [0]*(N+1)
    q=[]                #큐
    q.append(V)         #시작점
    visited[V]=1        #시작점 처리
    while q:
        V = q.pop(0)    #디큐
        print(V)        #visit(v)
        for w in adjlist[V]:  #인접하고 미방문 정점 w가있으면
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[V] + 1
    return  0

for _ in range(1):
    # tc 번호, 간선의 개수
    tc, E = map(int, input().split())
    arr = list(map(int, input().split()))
    adjlist = [[] for _ in range(100)]
    for i in range(E):
        a,b = arr[i*2], arr[i*2+1]
        adjlist[a].append(b)

    print(adjlist)

    bfs(0,99) # 시작, 마지막 정점 , 목표 정점