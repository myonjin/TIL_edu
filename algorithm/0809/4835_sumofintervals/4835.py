import sys
sys.stdin = open('input.txt')
TC = int(input())
for tc in range(1,TC+1):
    # N:숫자 개수 M:이웃한 M개
    N, M = map(int, input().split())
    arr=list(map(int, input().split()))
    arr_min_max=[]

    result=0

    for i in range(N-M+1):
        result=0
        for j in range(i,i+M):
            result+=arr[j]
        arr_min_max.append(result)

    for i in range(len(arr_min_max)-1,0,-1):
        for j in range(i):
            if arr_min_max[j]>arr_min_max[j+1]:
                arr_min_max[j],arr_min_max[j+1] = arr_min_max[j+1],arr_min_max[j]
    result=arr_min_max[-1]-arr_min_max[0]
    print(f"#{tc} {result}")





