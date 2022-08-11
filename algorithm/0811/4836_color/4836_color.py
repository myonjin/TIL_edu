import sys
sys.stdin = open("input.txt")

test = int(input())

for tc in range(1,test+1):
    A=[[0]*10 for _ in range(10)]
    N=int(input()) #네모 개수

    cnt=0
    for _ in range(N):
        r1,c1,r2,c2,col = map(int, input().split()) # 2,2,4,4,1
        for i in range(r1,r2+1):
            for j in range(c1,c2+1):
                A[i][j]+=col
    for i in range(10):
        for j in range(10):
            if A[i][j]==3:
                cnt+=1
    print(f"#{tc} {cnt}")


