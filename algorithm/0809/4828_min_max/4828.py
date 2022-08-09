import sys
sys.stdin = open('input.txt')

N = int(input())

for tc in range(1,N+1):
    T=int(input())
    num=list(map(int, input().split()))
    num_max=num[0]
    num_min=num[0]
    result=0
    for i in range(T):
        if num[i]>num_max:
                num_max=num[i]
        elif num[i]<num_min:
                num_min=num[i]
    result=num_max-num_min
    print(f"#{tc} {result}")
