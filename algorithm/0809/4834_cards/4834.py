import sys
sys.stdin = open('input.txt')

N = int(input())
for tc in range(1,N+1):
    T=int(input())
    num=int(input())
    result=0
    result_i=0
    c=[0]*10
    for i in range(T):
        c[num%10]+=1
        num//=10

    for i in range(10):
        if c[i]>=result:
            result=c[i]
            result_i=i
    print(f"#{tc} {result_i} {result}")


# 0123456789
# 0001211302
#
#       and 앞에꺼 >= 뒤에꺼
#          if