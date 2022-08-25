import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    T=int(input())
    M=list(map(int,input().split()))
    q=[]
    minus=[1,2,3,4,5]
    i = 0
    while M[0]>0:
        x=M.pop(0)
        M.append(x-minus[i%5])
        if x-minus[i%5]<=0:
            M[-1]=0
            break
        i += 1
    print(f'#{tc}',end=' '),print(*M)