# 이진탐색
import sys
sys.stdin = open('input.txt')


def binary_search(start, end, key):
    start = start
    end = end
    count = 0

    while start + 1 < end:
        middle = (start + end) // 2
        if middle == key:
            return count
        elif middle > key:
            end = middle
        else:
            start = middle
        count += 1

    if start == key:
        return count
    if end == key:
        return count + 1

T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    # A, B 각자 조사
    print(f'#{tc}', end=' ')
    a = binary_search(1, P, A)
    b = binary_search(1, P, B)
    print(a, b)

    # a가 더 오래 걸렸다면 b 승리
    if a > b or b == -1:
        print('B')
    elif a < b or a == -1:
        print('A')
    else:
        print(0)