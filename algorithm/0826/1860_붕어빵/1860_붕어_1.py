import sys
sys.stdin = open('input_1.txt')
T=int(input())
for tc in range(1,T+1):
    N,M,K=map(int,input().split()) #N명의 사람, M초의 시간을 들이면 K개의 붕어빵
    people=list(map(int,input().split())) # 사람이 몇초에 오는지
    err=False
    for i in people:                        # 아예 불가능 한 경우
        if i < M:
            print(f'#{tc} Impossible')
            err=True
            break
    if err == True:
        continue
    people.sort()
    stack=[]
    second=0
    bong=0
    cnt=0
    while cnt<100000:
        cnt+=1
        second+=1
        if second%M==0:
            while bong<K: #붕어빵 스택에 담기
                stack.append('붕어빵')
                bong+=1
        if not people:
            print(f'#{tc} Possible')
            err = True
            break
        if second==people[0]:
            if stack:
                people.pop(0)
                stack.pop()
            else:
                print(f'#{tc} Possible')
                err = True
                break
    if err == True:
        continue
