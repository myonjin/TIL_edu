from collections import deque
for tc in range(1,int(input())+1):
    arr=list(map(int,input().split()))
    P1=deque([])
    P1_box=[0]*10
    P2=deque([])
    P2_box=[0]*10
    result=0
    for i in range(len(arr)):
        if i in [0,2,4,6,8,10]:
            P1.append(arr[i])
            P1_box[arr[i]] += 1
            for j in P1_box:
                if j==3:
                    result+=1
                    break
            for k in range(len(P1_box)-2):     # 0 ~ 7
                if P1_box[k]>=1 and P1_box[k+1]>=1 and P1_box[k+2]>=1:
                    result+=1
                    break
        elif i in [1,3,5,7,9,11]:
            P2.append(arr[i])
            P2_box[arr[i]] += 1
            for j in P2_box:
                if j==3:
                    result+=2
            for k in range(len(P2_box)-2):
                if P2_box[k]>=1and P2_box[k+1]>=1 and P2_box[k+2]>=1:
                    result+=2
        elif result:
            break
    # print(P2)
    # print(P1_box,P2_box)
    if result==3:
        result=0
    print(f'#{tc} {result}')
