import sys
sys.stdin = open('input.txt')
from collections import deque
def f(i,k):
    global n
    if i == k:
        if sum(bit)==n-1:
            subset.append(bit.copy())
    else:
        bit[i] = 0
        f(i+1,k)
        bit[i] = 1
        f(i+1, k)

T=int(input())
for tc in range(1, T+1):
    n = int(input())  # 가로 세로
    arr = [list(map(int,input().split())) for _ in range(n)]
    subset=deque([])
    bit = [0]*((n-1)*2)
    f(0,(n-1)*2)
    min_sum=9999999
    # print(subset)
    # 0이면 밑으로 1이면 오른쪽으로
    for sub_2 in subset:
        i=0
        j=0
        result=arr[i][j]
        for sub in sub_2:
            if sub==0:
                i+=1
            elif sub==1:
                j+=1
            result+=arr[i][j]
            if result>=min_sum:
                break
        if result<=min_sum:
            min_sum=result
    print(f'#{tc} {min_sum}')