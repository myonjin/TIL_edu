from collections import deque
for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    sW=list(map(int,input().split()))
    sT=list(map(int,input().split()))
    W=sorted(sW,reverse=True)           #내림차순 정렬
    s1=sorted(sT,reverse=True)          #내림차순 정렬
    T=deque(s1)                         #deque
    result=0
    for w in W:
        if len(T)==0:                   #트럭 없으면 끝
            break
        if w>max(T):                    #적재량 초과한 화물은 패스
            continue
        else:
            result+=w
            T.popleft()
    print(f'#{tc} {result}')

