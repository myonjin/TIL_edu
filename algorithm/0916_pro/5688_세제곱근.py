T=int(input())
for tc in range(1,T+1):
    N=int(input())
    for i in range(1,10**6+1):
        num=i**3
        if num==N:
            print(f'#{tc} {i}')
            break
    else:
        print(f'#{tc} -1')

