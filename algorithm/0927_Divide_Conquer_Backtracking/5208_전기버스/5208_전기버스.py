import sys
sys.stdin = open('input.txt')

def f(i,k):
    global charge,min_charge
    if i == k:
        # print(bit)
        print(bit)
        charge = 0
        for i in range(len(bit)):
            if bit[i] == 1 and bit.count(1) - 1 <= min_charge:
                charge += arr[i]
                if charge >= N:
                    min_charge = bit.count(1) - 1
            else:
                continue


    else:
        bit[i] = 1
        if bit[0]==1:
            f(i+1,k)
            bit[i] = 0
            f(i+1, k)
            return




T=int(input())
for tc in range(1,T+1):
    N, *arr=list(map(int,input().split()))
    # print(N,arr)
    n = len(arr)
    bit = [0] * n
    bit[0] =1
    min_charge=999999
    charge=0
    f(0, n)
    print(f'#{tc} {min_charge}')