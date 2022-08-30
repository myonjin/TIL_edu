import sys
sys.stdin = open('input_1.txt')
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    que = list(map(int,input().split()))

    que.sort()

    result = 'Possible'
    bread = 0
    for i in range(N):
        bread = ((que[i]//M)*K) - i # 남아있는 붕어빵 = 지금 시간에 만든 붕어빵과 앞사람 것 뺀 만큼
        if bread - 1 < 0:
            result = 'Impossible'
            break
    print(f'#{tc} {result}')