import sys
sys.stdin = open('input.txt')
def sol(N, bus):
    dp = [0] * 1001
    for i in bus:
        if i[0] == 1:
            for j in range(i[1], i[2] + 1):
                dp[j] += 1
        if i[0] == 2:
            for j in range(i[1], i[2] + 1, 2):
                dp[j] += 1

        if i[0] == 3:
            if i[1] % 2:
                for j in range(i[1], i[2] + 1):
                    if j % 3 == 0 and j % 10 != 0:
                        dp[j] += 1
            else:
                for j in range(i[1], i[2] + 1):
                    if j % 4 == 0:
                        dp[j] += 1
    return max(dp)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {sol(N, bus)}')