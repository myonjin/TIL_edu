import sys

sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1):
    N, M = map(int, input().split())
    a = [list(input().split()) for _ in range(N)]
    result = ''

    for j in range(N):
        for i in range(0, N-M+1):
            x = a[j][i: i+M-1]
            y = a[j][i+M-1:i:-1]
            # print(a[j][4:2:-1])
            # print(x, y)
