import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    M,M=map(int, input().split())
    a=list(map(int,input().split()))
    b = list(map(int, input().split()))
    result=0
    max=0
    if len(a)<len(b):

        for i in range(len(b)-len(a)+1):
            max=0
            for j in range(len(a)):
                max+=a[j]*b[i+j]
            if max>result:
                result=max
    if len(a)>len(b):
        for i in range(len(a)-len(b)+1):
            max=0
            for j in range(len(b)):
                max+=b[j]*a[i+j]
            if max>result:
                result=max


    print(f'#{tc} {result}')




