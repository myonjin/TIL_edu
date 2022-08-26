for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 각 출발위치 x 값을 표시하면서 내려가고,
    # 같은곳을 지나가더라도 1. 0이 아니고 2. 자기 고유 값이 아니면 자기거를 덮어쓰고 지나간다.
    # 고유값은 2씩 더해서 ? x = 0 이면 2 저장, x = 4이면 6 저장 (0, 1 이미 쓰고있으니까)
    # BFS 활용하여 가장 먼저 도착하면 최단

    q = []
    for j in range(100):
        if arr[0][j] == 1:
            q.append([0, j])

    min_counts = [0, 100 * 100]
    for si, sj in q:
        visited = [[0] * 100 for _ in range(100)]
        counts = [sj, 0]

        while si < 100:
            visited[si][sj] = 1

            if sj - 1 >= 0 and arr[si][sj - 1] == 1 and visited[si][sj - 1] == 0:
                si, sj = si, sj - 1
            elif sj + 1 < 100 and arr[si][sj + 1] == 1 and visited[si][sj + 1] == 0:
                si, sj = si, sj + 1
            else:
                si, sj = si + 1, sj
            counts[1] += 1

        if counts[1] < min_counts[1]:
            min_counts = counts

    print(f'#{tc} {min_counts[0]}')