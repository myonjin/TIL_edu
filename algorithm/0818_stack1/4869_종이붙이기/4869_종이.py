import sys
sys.stdin=open('input.txt')

def rec(N):
    if N==10:
        return 1
    elif N==20:
        return 3
    else: return rec(N-10)+rec(N-20)*2;

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result=0

    print(f"#{tc} {rec(N)}")