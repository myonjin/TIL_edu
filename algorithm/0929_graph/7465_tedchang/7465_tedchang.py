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
    p = [i for i in range(N+1)]

    for _ in range(M):
        a,b=list(map(int,input().split()))
        union(a,b)

    result=[]
    for i in p:
        result.append(find_set(i))

    set(result)
    print(f'#{tc} {len(set(result))-1}')