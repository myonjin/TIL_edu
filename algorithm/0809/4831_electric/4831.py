import sys
sys.stdin = open('input.txt')
TC = int(input())
#K=이동가능 수 N=종점번호 M:충전기충전정류장수
for tc in range(1,TC+1):
    num=[]
    K, N, M =list(map(int,input().split()))
    num=list(map(int, input().split()))
    jung=[0]*(N+1)
    count=-1

    for i in num:
        jung[i]+=1 # 여기까지 기본 세팅
    if num[0]>K or N-num[-1]>K:
        count=0
    for i in range(len(num)-1):
        if num[i+1]-num[i]>K:
            count=0


    if count==-1:
        count=0
        h=0
        while True:
            if h+K>=N:
                break
            else:
                for i in (K+h,h,-1):
                    if i in num:
                        h=i
                        count+=1
                        break

    print(f"#{tc} {count}")



