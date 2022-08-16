import sys

sys.stdin = open('input.txt')

for tc in range(1, 2):
    T = int(input())
    arr = []
    for _ in range(100):
        arr.append(input())
    m = 100
    result = 0
    while m > 0:
        for i in range(100):
            for k in range(0, 101 - m):
                x_s = ''
                for j in range(k, m + k):
                    x_s += arr[j][i]

                if x_s == x_s[::-1]:
                    result = len(x_s)
                    break

        if result != 0: break;

        m -= 1
    print(f'#{tc} {result}')

