import sys
sys.stdin = open("input.txt")
for tc in range(1, 11):
    N=int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_value = 0
    # 행우선
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        if max_value < sum:
            max_value = sum

    # 열우선
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[j][i]
        if max_value < sum:
            max_value = sum
    # 대각선 \
    sum = 0
    for i in range(100):
        sum += arr[i][i]
        if max_value < sum:
            max_value = sum
    # print(sum_value)

    # 대각선 /
    sum = 0
    for i in range(100):
        sum += arr[i][99 - i]

        if max_value < sum:
            max_value = sum
    # print(sum_value)
    print(f"#{tc} {max_value}")