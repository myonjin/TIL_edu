import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = input(), input()
    # map(func, iterable)
    result = max(map(lambda x : M.count(x), set(N)))

    print(f'#{tc} {result}')