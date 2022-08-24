import sys
sys.stdin = open('input.txt')



for tc in range(1,2):
    T=int(input())
    num=list(map(int, input().split()))
    num_max=num[0]
    num_min=num[0]
    index_max=0
    index_min=0
    result=0
    c=0
    print(num)
    while c<=T:
        for i in range(len(num)-1, 0, -1):
            for j in range(i):
                if num[j] > num[j + 1]:
                    num[j], num[j + 1] = num[j + 1], num[j]

        num_max=num[-1]
        num_min=num[0]
        index_max = num.index(num_max)
        index_min = num.index(num_min)
        num[index_max]-=1
        num[index_min]+=1
        c+=1
        result=num_max-num_min

    print(f"#{tc} {result}")


