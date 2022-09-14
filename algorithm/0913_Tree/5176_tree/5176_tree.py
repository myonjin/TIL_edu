
T=int(input())
def inorder(n):
    global cnt,result1,result2
    if n<=V:
        inorder(n*2)
        cnt+=1
        if n==1: #왼쪽 다봤으면
            result1=cnt  #루트노트 계산
        if n==V//2:     #마지막노드의 부모노드
            result2=cnt
        inorder(n*2+1)

for tc in range(1,T+1):
    V=int(input())
    cnt=0
    result1=0
    result2=0
    inorder(1)
    print(f'#{tc} {result1} {result2}')