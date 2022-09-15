import sys
sys.stdin = open('input.txt')
def inorder(n):
    if n <= V:                      # 자식두명을 계산해준값을 부모 노드로
        if node[n]=='+':
            node[n] = inorder(ch1[n]) + inorder(ch2[n])
        if node[n]=='-':
            node[n] = inorder(ch1[n]) - inorder(ch2[n])
        if node[n]=='*':
            node[n] = inorder(ch1[n]) * inorder(ch2[n])
        if node[n]=='/':
            node[n] = inorder(ch1[n]) // inorder(ch2[n])
        return node[n]


for tc in range(1,11):
    V=int(input())# 정점의 개수(마지막 번호)
    node=[0]*(V+1)# 노드가 가진값
    ch1=[0]*(V+1)
    ch2=[0]*(V+1)

    for _ in range(V):
        arr=list(input().split())
        if len(arr)==4:                         # 사칙연산일때 사칙연산,노드자식값넣어줌
            node[int(arr[0])] = arr[1]
            ch1[int(arr[0])] = int(arr[2])
            ch2[int(arr[0])] = int(arr[3])
        else:
            node[int(arr[0])] = int(arr[1])     # 노드가 가진값넣어줌
    print(f'#{tc} {inorder(1)}')