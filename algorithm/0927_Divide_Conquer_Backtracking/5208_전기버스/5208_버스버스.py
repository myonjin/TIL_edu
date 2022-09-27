import sys
sys.stdin = open('input.txt')


def bus(start,cnt):
    global result
    if cnt>=result:
        return 0

    if start>=N:
        if result>cnt:
            result=cnt
        return 0


    for i in range(1,arr[start]+1):    # 1, 2 range(1,3)
        bus(start+i,cnt+1)



T=int(input())
for tc in range(1,T+1):
    N, *arr=list(map(int,input().split()))
    arr= [0] + arr + [0]    # 정류장 1부터 N까지 (인덱스)
    print(arr)
    cnt=0
    result=N
    # print(arr)
    bus(1,cnt)
    print(f'#{tc} {result-1}')