import sys
sys.stdin = open('input.txt')
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    numbers = sorted(list(set([input() for _ in range(N)])))
    numbers.pop(0)
    print(numbers)
