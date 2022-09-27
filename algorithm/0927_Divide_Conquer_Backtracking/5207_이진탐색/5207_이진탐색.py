import sys
sys.stdin = open('input.txt')

def binary_search(arr,start,end,key):
    global cnt
    mid = (start + end ) //2

    if start > end:
        return 0
    if arr[mid] == key:
        return 1

    elif (not cnt or cnt=='R' ) and arr[mid] > key:
        cnt='L'
        return binary_search(arr,start,mid - 1 , key)
    elif (not cnt or cnt=='L' ) and arr[mid] < key:
        cnt='R'
        return binary_search(arr,mid + 1,end , key)
    return 0
T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()

    result=0
    for i in B:
        cnt=''
        result+=binary_search(A,0,N-1,i)
    print(f'#{tc} {result}')
