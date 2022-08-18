def fibo_dp(n):
    table[0]=0
    table[1]=1
    for i in range(2,n+1):
        table[i] = table[i-1]+table[i-2]
    return
table=[0]*101
fibo_dp(100)
print(table[20])

t= int(input())
for tc in range(1,t+1):
    n= int(input())
    print(f'#{tc} {table[n]}')