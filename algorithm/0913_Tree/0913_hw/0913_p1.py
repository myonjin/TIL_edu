def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])
def find_root(n):
    for i in range(1,V+1):
        if par[i]==0:
            return i
V= int(input())
arr= list(map(int,input().split()))

ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
par = [0] * (V+1)
for i in range(V-1):
    p,c = arr[i*2],arr[i*2+1]
    if ch1[p]==0:
        ch1[p]=c
    else:
        ch2[p]=c
    par[c] = p

preorder(find_root(V))
