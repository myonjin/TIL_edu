import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    target, pattern = input().split()

    result = len(target) - (target.count(pattern) * (len(pattern) - 1))