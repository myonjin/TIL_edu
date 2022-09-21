def selectionSort(A,s):
    n=len(A)
    if s==n-1:
        return
    min =s
    for i in range(s,n):
        if A[min]>A[i]:
            min = i
    A[s],A[min] = A[min],A[s]

    selectionSort(A,s+1)

A=[4,2,5,6,1,2]
selectionSort(A,0)
print(A)