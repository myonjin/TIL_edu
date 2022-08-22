import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input()))

    count = [0]*10
    for char in ai:
        count[char] += 1

    # 최대 출현 횟수
    max_count = 0
    # 가장 큰 수
    max_val = 0
    for i in range(10):
        # 최대 출현 횟수가 count의 i번째보다 작거나 같다면
        # 작거나 같아야 하는 이유는 뭘까?
        if max_count <= count[i]:
            max_count = count[i]
            max_val = i

    print(f'#{tc} {max_val} {max_count}')