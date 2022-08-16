import sys
sys.stdin = open('input.txt')

def reverse_char(N, arr) :
    for M in range(N,0,-1) :
        # 가로
        for i in range(N):
            for st in range(0, N - M + 1):  # 시작위치 될 수 있는 범위
                if arr[i][st] != arr[i][st + M - 1]:
                    continue
                elif arr[i][st + 1:st + M - 1] == arr[i][st + M - 2:st:-1]:
                    return arr[i][st:st + M]

        # # 세로
        # for j in range(N):
        #     char = ''
        #     for i in range(N):  # j 같은 값 (세로줄) 한줄씩 뽑아서
        #         char += arr[i][j]  # char 에 저장 / j=0, 1, 2,.. 일 때 세로줄
        #
        #     for st in range(0, N - M + 1):  # char에서 검사 시작할 위치 설정
        #         if char[st] != char[st + M - 1]:
        #             continue
        #         elif char[st + 1:st + M - 1] == char[st + M - 2:st:-1]:
        #             return char[st:st + M]


for _ in range(10) :
    tc = int(input())
    N = 100

    arr = []
    for _ in range(N) :
        arr.append(input())

    result = len(reverse_char(N, arr))
    print(f'#{tc} {result}')