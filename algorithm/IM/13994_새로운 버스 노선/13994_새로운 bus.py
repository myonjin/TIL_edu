import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    bus=[list(map(int,input().split())) for _ in range(n)]
    arr=[0]*1001
    for bs in bus:
        if bs[0]==1:
            for i in range(bs[1],bs[2]+1):
                arr[i]+=1
        elif bs[0] == 2:
            for i in range(bs[1],bs[2],2):
                arr[i]+=1
            arr[bs[2]]+=1
        elif bs[0] == 3:
            if bs[1]%2==0: #짝수
                for i in range(0,bs[2],4):
                    if bs[1]<i<bs[2]:
                        arr[i]+=1


            elif bs[1]%2==1: #홀수
                for i in range(0,bs[2],3):
                    if bs[1]<i<bs[2] and i%10!=0:
                        arr[i]+=1

            arr[bs[1]] += 1
            arr[bs[2]] += 1
    print(f'#{tc} {max(arr)}')
