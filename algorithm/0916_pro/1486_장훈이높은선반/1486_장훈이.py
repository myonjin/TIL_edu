import sys
sys.stdin = open('input.txt')
from itertools import combinations

T=int(input())
for tc in range(1,T+1):
    N,B=map(int,input().split())
    arr=list(map(int, (input().split())))
    arr_subset=[]
    min_result=10000000
    for i in range(1,len(arr)+1):
        a=list(combinations(arr,i))
        for m in set(a):
            if sum(m)>=B:
                result=sum(m)-B
                if min_result>result:
                    min_result=result
    print(f'#{tc} {min_result}')