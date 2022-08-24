import sys
sys.stdin=open('input_miro.txt')
T=int(input())

for tc in range(1,T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]