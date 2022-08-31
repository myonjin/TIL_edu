Number=int(input())
def divisor(N):
    result=0
    for i in range(1,N+1):
        if N%i==0:
            result+=str(i)+" "
    return result
print(divisor(Number))

            