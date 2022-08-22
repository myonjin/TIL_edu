import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0
    arr = list(range(1,13))

    for i in range(1<<len(arr)):
        tmp = []
        for j in range(len(arr)):
            if i & (1<<j):
                tmp.append(arr[j])
        if len(tmp) == N and sum(tmp) == K:
            result += 1

    print(f'#{tc} {result}')