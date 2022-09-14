def enq(n):
    global last
    last+=1
    heap[last]=n
    c=last
    p=c//2
    while p and heap[c] < heap[p]:
        heap[p],heap[c]=heap[c],heap[p]
        c = p
        p = c//2
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=list(map(int,input().split()))
    heap=[0]*100
    last= 0
    result=0
    for i in arr:
        enq(i)
    while N:
        result+=heap[N//2]
        N=N//2
    print(f'#{tc} {result}')