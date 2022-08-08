import sys
sys.stdin = open('input.txt')

N = int(input())

for tc in range(1, N+1):
    # 상자들이 담겨있는 칸의 개수
    A = int(input())
    numbers = list(map(int, input().split()))


    result = 0
    for i in range(A):
        # i 0부터 계산 시작 아무것도 없다치고 최대값
        # 전체길이 - ( i 인덱스값 + 1)
        max_h = len(numbers)-(i+1)


        for j in range(i+1, len(numbers)):
            if numbers[i] <= numbers[j]:

                max_h -= 1
            # 같거나 큰높이는 방해 됨으로 하나마다 -1 씩 해준다
        if result < max_h:
            result = max_h
            # 큰 최대값이 나올때마다 result 에 넣어준다
    print(f'#{tc} {result}')
