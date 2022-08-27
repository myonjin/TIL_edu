import sys
sys.stdin = open('input.txt')
T=int(input())
for _ in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]

