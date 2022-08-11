import sys
sys.stdin = open("input.txt")

test = int(input())
for tc in range(1, test+1):

    N,K=map(int,input().split())
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,]
    result = []
    end=0
    for i in range(1 << len(arr)):
        subset = []

        for j in range(len(arr)):
            if i & (1 << j):
                subset.append(arr[j])
        if len(subset)==N:
            result.append(subset)
    for i in result:
        sum=0
        for j in range(N):
            sum+=int(i[j])
        if sum==K:
            end+=1

    print(f"#{tc} {end}")
