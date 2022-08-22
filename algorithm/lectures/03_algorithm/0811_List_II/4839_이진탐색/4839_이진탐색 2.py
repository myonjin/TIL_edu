import sys
sys.stdin = open('input.txt')

def binary_search(start, end, target, cnt):
    if start + 1 == end:
        if start == target:
            return cnt
        if end == target:
            return cnt + 1

    middle = (start + end) // 2
    if middle == target:
        return cnt
    else:
        if middle < target:
            # 중간지점부터 시작해야 한다는 조건 필수 확인
            return binary_search(middle, end, target, cnt + 1)
        else:
            return binary_search(start, middle, target, cnt + 1)



T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    # A, B 각자 조사
    print(f'#{tc}', end=' ')

    try:
        a = binary_search(1, P, A, 0)
    except RecursionError:
        a = -1

    try:
        b = binary_search(1, P, B, 0)
    except RecursionError:
        b = -1

    # a가 더 오래 걸렸다면 b 승리
    if a > b or a == -1:
        print('B')
    elif a < b or b == -1:
        print('A')
    else:
        print(0)

