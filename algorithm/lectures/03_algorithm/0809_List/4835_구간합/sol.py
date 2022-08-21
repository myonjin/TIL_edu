import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    init = 0
    for i in range(M):
        init += arr[i]

    max_v = min_v = init

    # 전체 길이 N중에, m+1만큼 제외
    for i in range(N-M+1):
        # 내 위치 -> i 부터 i+m번까지 값들을 더할 거다.
        # 더해 나갈 임시 값
        tmp = 0
        for j in range(i, i+M):
            tmp += arr[j]

        # 최대, 최소값 초기화
        if tmp > max_v:
            max_v = tmp
        if tmp < min_v:
            min_v = tmp

    # 최소, 최댓값의 차
    result = max_v-min_v
    print(f'#{tc} {result}')