import sys
sys.stdin = open('input.txt')

def dfs(n):
    # 출발지 0을 방문 표시
    visited[n] = 1

    # 0에서 출발하므로 1부터 조사
    for w in range(1, 101):
        # n(출발지)에서 w(다음 행성지)로 이동 가능여부 파악
        # 0 2 -> G[0][2]에 True 표시 해 두었음
        # 이전에 방문한 적 없는 곳만 방문
            # 어느쪽에서 왔든 99에 도착만하면 되므로 
            # 한명이라도 방문한 적 있다면 상관 X
        if G[n][w] == 1 and visited[w] == 0:
            # n에서 w로 이동하였으므로 w 부터 다시 조사
            dfs(w)

# tc 10개
for _ in range(10):
    # tc 번호, 간선의 개수
    tc, E = map(int, input().split())
    # 이동 가능 정보
    data = list(map(int, input().split()))

    # 방문 표시 할 리스트 (정점 최대 100개)
    visited = [0] * 101

    # 인접 행렬 
    G = [[0 for _ in range(101)] for _ in range(101)]

    # 넘겨받은 이동 가능 정보는 순서쌍으로 이루어 져있음
    # 2개가 한 세트로, 0 2는 0번에서 2번으로 이동 가능의 의미
    # 방향성 그래프 이므로, 한쪽 방향으로만 체크
    for i in range(0, len(data), 2):
        G[data[i]][data[i+1]] = 1
    
    dfs(0)

    print(f'#{tc} {visited[99]}')