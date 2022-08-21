import sys
sys.stdin = open('input.txt')

for i in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    # 행 우선
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[i][j]
        if result < tmp:
            result = tmp

    # 열 우선
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += arr[j][i]
        if result < tmp:
            result = tmp

    # 좌상 우하
    tmp = 0
    for i in range(100):
        tmp += arr[i][i]
    if result < tmp:
        result = tmp

    # 우상 좌하
    tmp = 0
    for i in range(100):
        # print(i, 99-i)
        tmp += arr[i][99-i]
    if result < tmp:
        result = tmp

    print(f'#{tc} {result}')
