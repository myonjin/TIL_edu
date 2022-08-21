import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    pattern, target = input(), input()
    print(f'#{tc}', 1) if pattern in target else print(f'#{tc}', 0)