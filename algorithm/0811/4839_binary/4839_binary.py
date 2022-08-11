import sys
sys.stdin = open("input.txt")

test = int(input())
result=0
win=''
def binarySearch(arr, s, P , key, cnt=1):

    if s > P:
        return 0
    else:
        middle = (s + P) // 2
        # print(middle, arr[middle])
        if arr[middle] == key:
            return cnt
        elif arr[middle] > key:
            return binarySearch(arr, s, middle, key,cnt+1)
        else:
            return binarySearch(arr, middle, P, key,cnt+1)

for tc in range(1, test+1):

    P,Pa,Pb=map(int,input().split())
    arr = list(range(1,P+1))
    N = len(arr)
    cnt_a=binarySearch(arr,0,P-1,Pa)
    cnt_b=binarySearch(arr, 0 ,P-1,Pb)

    if cnt_a==cnt_b:
        print(f"#{tc} {0}")

    elif cnt_a>cnt_b:
        print(f"#{tc} B")

    elif cnt_a<cnt_b:
        print(f"#{tc} A")




