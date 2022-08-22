T = int(input())

for tc in range(1, T+1):
    N = int(input())
    r1, c1, r2, c2 = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sumV = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            sumV += arr[i][j]

    avgV = sumV // ((r2-r1+1)*(c2-c1+1))
    result = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            result += abs(arr[i][j] - avgV)
    print(result)