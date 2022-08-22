import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    tickets = list(map(int, input().split()))
    plans = list(map(int, input().split()))
