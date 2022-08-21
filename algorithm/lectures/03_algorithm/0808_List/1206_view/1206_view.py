import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    data = list(map(int, input().split()))
    result = 0

    # 앞, 뒤 2칸 제외 (좌, 우 2칸에는 건물이 없음)
    for i in range(2, N - 2):
        # 각 층간의 높이 차이중, 가장 차이가 적은값
        min_value = 256
        # 나를 기준으로 앞 2칸, 뒤 2칸을 계산해야 하므로 5
        for j in range(5):
            if j != 2:  # 내가 아니라면
                # 내 위치 (i) - 내 위치 -2 + 현재 조사 중인 값의 차
                # 최솟 값보다 적으면
                if data[i] - data[i - 2 + j] < min_value:
                    min_value = data[i] - data[i - 2 + j]
        # 그 차이가 양수면
        if min_value > 0:
            result += min_value
    print(f'#{tc} {result}')