def func(r, c):
    for i in range(1, N - r - 1):  # 오른쪽 아래로 가는 횟수

        if i + c >= N:  # 맨 오른쪽의 카페 위치
            # print(r, c, '에서 i', i, '는 안돼')
            break
        for j in range(1, N - r - i):  # 왼쪽 아래로 가는 횟수 (범위는 맨 아래의 카페 위치까지)
            if c - j < 0:  # 맨 왼쪽의 카페 위치
                # print(r, c, i, '에서 j', j, '는 안돼')
                break
            # print(r, c, i, j, '는 여기까지 왔다.')
            # print(N, r, c, i, j)
            # 고려할 가치가 있을 때
            cafes = set()
            nr, nc = r, c
            for d1 in range(1, i + 1):
                nr += 1
                nc += 1
                cafes.add(arr[nr][nc])
            for d2 in range(1, j + 1):
                nr += 1
                nc -= 1
                cafes.add((arr[nr][nc]))
            for d3 in range(1, i + 1):
                nr -= 1
                nc -= 1
                cafes.add(arr[nr][nc])
            for d4 in range(1, j + 1):
                nr -= 1
                nc += 1
                cafes.add(arr[nr][nc])
            cafe_len = len(set(cafes))
            if (i + j) * 2 == len(set(cafes)):
                global answer
                if answer < cafe_len:
                    answer = cafe_len

    # print(r, c, '는 이제 끝')


directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    answer = -1  # 정답을 저장할 변수
    # 가장 위의 점을 (r, c)라고 할 때
    for r in range(N - 2):
        for c in range(1, N - 1):
            func(r, c)

    print(f'#{tc} {answer}')