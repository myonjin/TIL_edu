import sys
sys.stdin = open("input.txt")
test = int(input())
def selectionsort(a,N):
    for i in range(10):
        minidx=i
        for j in range(i+1,N):
            if i%2==0:

                if a[minidx] < a[j]:
                    minidx = j
            else :
                if a[minidx] > a[j]:
                    minidx = j

        a[i], a[minidx]=a[minidx],a[i]

for tc in range(1, test+1):
    N=int(input())
    A=list(map(int, input().split()))
    selectionsort(A,len(A))
    print(f"#{tc}", end=" ")
    for i in range(10):
        print(A[i],end=" ")
    print()


