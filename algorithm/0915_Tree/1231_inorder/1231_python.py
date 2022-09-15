import sys
sys.stdin = open('input.txt')
def inorder(n):
    if n<=V:            #중위순회로 출력
        inorder(2*n)
        print(node[n],end='')
        inorder(2*n+1)

for tc in range(1,11):
    V=int(input())
    node=[0]*(V+1)
    for i in range(1,V+1):
        arr=list(input().split())
        node[i]=arr[1]          #노드의 정보에 알파벳담음
    print(f'#{tc}',end=' ')
    inorder(1)
    print()

