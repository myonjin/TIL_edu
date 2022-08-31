import sys
sys.stdin=open('input.txt')
sqr=[list(map(int,input().split())) for _ in range(4)]
arr=[[0]*100 for _ in range(100)]
a=1
for c1,r1,c2,r2 in sqr:
    for c in range(c1,c2):
        for r in range(r1,r2):
            if arr[c][r]==0:
                arr[c][r]=1
sum=0
for i in range(100):
    for j in range(100):
        sum+=arr[i][j]
print(sum)