import sys
sys.stdin = open('input.txt')
T=int(input())
def postorder(n):
    if n>V:              #인덱스 범위 넘어가면
        return 0
    elif tree[n]:         #이미 tree에 값이 있으면
        return tree[n]
    elif n<=V:              # 자식노드 두명을 부모에 합쳐줌
        tree[n] = postorder(2*n) + postorder(2*n+1)
        return tree[n]


for tc in range(1,T+1):
    V,M,N=map(int,input().split()) #노드개수,리프노드,출력할노드번호
    tree=[0]*(V+1)
    for _ in range(M):
        a,b = map(int,input().split())
        tree[a]=b
    postorder(1)
    # print(tree)
    print(f'#{tc} {tree[N]}')