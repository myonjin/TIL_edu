from collections import deque
for tc in range(1,int(input())+1):
    N=int(input())
    s_e_first=[list(map(int,input().split())) for _ in range(N)]
    s_e=deque(sorted(s_e_first,key=lambda x:x[1]))         # 종료시간 기준으로 정렬해준다 lamda식 참고
    result=deque([])                                       # 무지성 deque에 담아준다
    for arr in s_e:
        arr=deque(arr)
        if not result:                                      #화물운반 리스트에 아무값이 없으면 추가 (맨처음추가)
            result.append(arr)
            continue
        else:
            if arr[0]<result[-1][1]:                        #종료시간보다 넣을 값의 시작시간이 작으면 패스
                continue
            elif arr[0]>=result[-1][1]:                     #종료시간과 같거나 뒤면 추가가능
                result.append(arr)
    print(f'#{tc} {len(result)}')

