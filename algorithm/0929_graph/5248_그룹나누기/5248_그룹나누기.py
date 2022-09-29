import sys
sys.stdin = open('input.txt')

def find_set(n):
    if n==p[n]:
        return n
    else:
        return find_set(p[n])

def union(a,b):
    p[find_set(b)]=find_set(a)

T=int(input())
for tc in range(1,1+T):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    p = [i for i in range(N+1)]
    result=[]

    for i in range(M):
        a,b = arr[2*i],arr[2*i+1]
        union(a,b)

    for i in p:
        result.append(find_set(i))
    set(result)
    print(f'#{tc} {len(set(result))-1}')