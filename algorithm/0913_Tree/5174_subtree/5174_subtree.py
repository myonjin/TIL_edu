import sys
sys.stdin = open('input.txt')

T=int(input())
def preorder(n):                #노드 탐색할대마다 노드의 개수를 추가해줌
    global cnt
    if n:
        cnt+=1
        preorder(ch1[n])
        preorder(ch2[n])
    return cnt
for tc in range(1,T+1):
    E,N=map(int,input().split())
    arr=list(map(int,input().split()))
    V=E+1 # 노드의 개수
    cnt=0 # 서브트리의 개수
    ch1=[0]*(V+1)
    ch2=[0]*(V+1)
    for i in range(E):
        p,c=arr[2*i],arr[2*i+1]
        if ch1[p]==0:
            ch1[p]=c
        else:
            ch2[p]=c

    print(preorder(N))
    # print(f'#{tc} {cnt}')


