from itertools import permutations
T=int(input())
for tc in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    a = [i for i in range(1, N + 1)]
    result=0
    min_result=999999
    for p in permutations(a,N):
        if p[0]==1:
            result=0
            for i in range(len(p)):  # 0 , 1 , 2  [1,2,3]
                if result >= min_result:
                    break
                if i == len(p) - 1:
                    result += arr[p[i] - 1][p[0] - 1]
                else:
                    result += arr[p[i] - 1][p[i + 1] - 1]
            else:
                if result <= min_result:
                    min_result = result
    print(f'#{tc} {min_result}')
