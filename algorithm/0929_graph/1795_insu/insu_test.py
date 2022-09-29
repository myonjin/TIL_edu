import sys

sys.stdin = open('input.txt')


def dijkstra(N, X, adj, d):
    visited = [0] * (N + 1)
    for i in range(N + 1):
        d[i] = adj[X][i]  # X에서 i로가는거(직진에서 가는값 미리담아준다) (빙빙돌아서 가는거말고)
    visited[X] = 1  # 출발해주는거 선택

    for _ in range(N - 1):  # N-1번만 반복해주면된다
        w = 0  #
        for i in range(1, N + 1):  # 1부터 N노드 넣어줘서
            if visited[i] == 0 and d[i] < d[w]:  # X를 제외한 X에서 정점가는거중 작은거
                w = i
        visited[w] = 1  # 그 정점은 해결했다.

        for v in range(1, N + 1):  # 정점 i가
            if 0 < adj[w][v] < 100000:  # w 가 갈수있으면
                if d[v]>d[w]+adj[w][v]:
                    d[v] = d[w] + adj[w][v]

                # 2에서 직빵으로 가는거와 2에서 다른곳을 거쳐서 가는것중 뭐가 가까운지


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())  # N 노드개수,M입력값,X생파집
    adj1 = [[100000] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):  # 자기 자신에게 가는비중 0
        adj1[i][i] = 0
    for _ in range(M):
        x, y, c = map(int, input().split())  # X -> Y 로 가고 C 만큼 비중
        adj1[x][y] = c  # 방향이 정해져있다.
    visited = [0] * (N+1)
    # print(*adj1,sep='\n')
    result = []
    distance = [0] * (N + 1)  # X에서 각 번호로 가는
    distance_2 = [0] * (N + 1)  # 각 번호가 X로 오는거
    dijkstra(N, X, adj1, distance)  # X에서  가는거 담아줌
    for i in range(1, N + 1):  # 1부터 N번호까지 각 노드별 최소비용
        if i==X:
            continue
        dijkstra(N, i, adj1, distance_2)
        # print(distance_2)  # 리스트에담아준다
        result.append(distance_2[X] + distance[i])  # i에서 X가는비용 + X에서 i 가는 비중
    # print(distance)
    # print(result)
    # print(visited)
    print(f'#{tc} {max(result)}')