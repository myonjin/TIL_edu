import sys

sys.stdin = open('input.txt')

T = int(input())

# 회문판독 함수
def palindrome(args):
    if args == args[-1::-1]:
        return True
    else:
        return False

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N * N 행렬에서 길이 M인 회문을 찾자
    arr = [list(input()) for _ in range(N)] # N * N 행렬 받아옴

    # N * N 행렬을 행 우선, 열 우선으로 각각 조회하며 회문을 찾아보자
    # 길이 M에 해당하는 회문은 단 하나만 존재한다고 한다

    for i in range(N):
        for j in range(N-M+1): # [i][j]의 인덱싱을 위해, 행 우선 먼저
            # [i][j] 지점에서 길이 M만큼 슬라이싱 한 후, 회문인지 아닌지 판독하자
            k = arr[i][j:j+M]
            if palindrome(k):
                ans = ''.join(k)
                print(f'#{tc} {ans}')


    # 이제 열 우선으로 돌아보자
    # 행렬을 돌려보자

    real_list = []
    lis_t = []
    for ii in range(N):
        for jj in range(N):
            lis_t += [arr[jj][ii]] # 열 우선 조회로 들어감
            if len(lis_t) == N: # lis_t 길이 N 될때마다
                real_list += [lis_t] # 해당 lis_t를 빈 리스트에 넣어주고
                lis_t = [] # Lis_t 초기화해줌

    # 위에서 해준거 똑같이 한번 더 해주면 됨
    for iii in range(N):
        for jjj in range(N-M+1):
            kk = real_list[iii][jjj:jjj+M]
            if palindrome(kk):
                an_s = ''.join(kk)
                print(f'#{tc} {an_s}')