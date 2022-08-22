import sys
from pprint import pprint
sys.stdin = open('input.txt')

T = int(input())

arr = [[0 for _ in range(11)] for _ in range(11)]
for i in range(10):
    for j in range(i + 1):
        if j == 0 or i == j:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
# print(arr)
            
# pprint(arr)
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i + 1):
            print(f'{arr[i][j]}', end=" ")
        print()