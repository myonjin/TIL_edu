def preorder(n):
    if  not n=='.':
        print(n,end='')
        preorder(tree[n][0])
        preorder(tree[n][1])

def inorder(n):
    if  not n=='.':
        inorder(tree[n][0])
        print(n,end='')
        inorder(tree[n][1])


def postorder(n):
    if  not n=='.':
        postorder(tree[n][0])
        postorder(tree[n][1])
        print(n,end='')

V=int(input()) #노드개수
tree=dict()
for _ in range(V):
    a,b,c=input().split()
    tree[a]=[b,c]

# print(tree['A'][0])
preorder('A')
print()
inorder('A')
print()
postorder('A')
