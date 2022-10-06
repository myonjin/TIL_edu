K,N=map(int,input().split())
arr=[int(input()) for _ in range(K)]
# print(arr)
result=0
ma_x=0
for i in range(1,min(arr)):
    result=0
    for j in arr:
        result+=j//i
    if result==N and ma_x<i:
        ma_x=i
print(ma_x)

