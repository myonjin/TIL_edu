import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    N,K=map(int,input().split()) # 수강생수, 과제를 제출한 사람수
    arr=list(map(int,input().split()))
    print(f'#{tc} ',end='')
    for i in range(1,N+1):
        if i not in  arr:
            print(f'{i}',end=' ')
    print()