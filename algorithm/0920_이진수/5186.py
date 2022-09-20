T=int(input())
for tc in range(1,T+1):
    N=float(input())
    cnt=0
    result=''
    while cnt<12:
        N=N*2
        if N>=1:
            N=N-1
            result+='1'
            if N==0:
                break
        else:
            result+='0'
        cnt+=1
    if cnt==12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {result}')
