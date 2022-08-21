import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0]
    min_v = arr[0]

    for i in range(len(arr)):
        if i == 0:
            continue
        if arr[i] > max_v:
            max_v = arr[i]
        if arr[i] < min_v:
            min_v = arr[i]

    result = max_v - min_v
    print(f'#{tc} {result}')
