import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    n=int(input()) #총 길이
    arr=[list(map(int,input().split())) for _ in range(n)]
    area=[] #행렬이 저장될곳
    for i in range(n):

