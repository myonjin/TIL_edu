import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())        #화덕 용량,피자의 개수
    arr = list(map(int, input().split()))   #입력값
    q=[]
    q_i=[]
    arr_i=[]
    for oo in range(1,M+1):
        arr_i.append(oo)
    # print(arr_i)   # [1,2,3,4,5]      #피자 번호

    for c in range(N):
        q.append(arr[c])
    # print(q)  [7,2,6]
    for zz in range(N):
        q_i.append(arr_i[zz])
    # print(q_i) [1,2,3]
    while len(q)>1:
        x=q.pop(0)
        q.append(x//2)
        x_i = q_i.pop(0)
        q_i.append(x_i)       #맨뒤에 오는걸 한바퀴 돈것으로 한다
                              #치즈를 2로 나누어 준다

        if q[-1]==0:            #치즈가 0이면
            q.pop()             #빼준다
            q_i.pop()
            if c+1<M:           #아직 안 구운피자가 남아있으면
                c=c+1           #추가해준다
                q.append(arr[c])
                q_i.append(arr_i[c])
    print(f'#{tc} {q_i[0]}')












