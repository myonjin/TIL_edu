import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=list(map(int,input().split()))
    arr_1=list(map(int,input().split()))
    arr_2=list(map(int,input().split()))
    arr_1_s=[]
    arr_2_s=[]
    if arr_1[0]%2==0:   #짝수
        arr_1_s.append(arr_1[0])
        arr_1_s.append(arr_1[-1])
        for i in range(1,len(arr_1)-1):
            if arr_1[i]%2==0:
                arr_1_s.append(arr_1[i])

    elif arr_1[0]%2==1:
        arr_1_s.append(arr_1[0])
        arr_1_s.append(arr_1[-1])
        for i in range(1, len(arr_1) - 1):
            if arr_1[i] % 2 == 1:
                arr_1_s.append(arr_1[i])

    #======================================
    if arr_2[0]%2==0:   #짝수
        arr_2_s.append(arr_2[0])
        arr_2_s.append(arr_2[-1])
        for i in range(1,len(arr_2)-1):
            if arr_2[i]%4==0:
                arr_2_s.append(arr_2[i])

    elif arr_2[0]%2==1:   #홀수
        arr_2_s.append(arr_2[0])
        arr_2_s.append(arr_2[-1])
        for i in range(1,len(arr_2)-1):
            if arr_2[i]%3==0 and arr_2[i]%10 != 0:
                arr_2_s.append(arr_2[i])
    # print(arr)
    # print(arr_1_s)
    # print(arr_2_s)
    #========================================
    max_arr=0
    for i in range(len(arr)):
        for j in range(len(arr_1_s)):
            if arr[i]==arr_1_s[j]:
                max_arr+=1
            break
        if max_arr==1:
            break
    max_arr_2=0
    for i in range(len(arr)):
        for j in range(len(arr_2_s)):
            if arr[i]==arr_2_s[j]:
                max_arr_2+=1
            break
        if max_arr_2==1:
            break
    # print(max_arr)
    # print(max_arr_2)
    if max_arr_2+max_arr>0:
        print(f'#{tc} {max_arr+max_arr_2+1}')
    if max_arr_2+max_arr==0:
        print(f'#{tc} 0')
