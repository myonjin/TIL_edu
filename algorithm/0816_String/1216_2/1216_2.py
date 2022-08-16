import sys
sys.stdin = open('input.txt')

def reverse_char(arr) :
    # 가로
    m=100
    while m > 0:
        for  i in range(0, 100-m+1): # 가로 첫줄, 2번째줄 3번째줄
            x=arr[i:100-i]
            arr[i:100-i]


            if arr[0:100]==x[::-1]:
                result=arr[0:100]
                break


    # 세로
    for j in range(N):
        char = ''
        for i in range(N):  # j 같은 값 (세로줄) 한줄씩 뽑아서
            char += arr[i][j]  # char 에 저장 / j=0, 1, 2,.. 일 때 세로줄

        for st in range(0, N - M + 1):  # char에서 검사 시작할 위치 설정
            if char[st] != char[st + M - 1]:
                continue
            elif char[st + 1:st + M - 1] == char[st + M - 2:st:-1]:
                return char[st:st + M]
    m-=1

    print(f'#{tc} {result}')




for tc in range(1, 11):
    T = int(input())
    arr = []
    for _ in range(N) :
        arr.append(input())

