T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pattern = [list(map(int, input().split())) for _ in range(3)]

    result = 0
    for i in range(N-2):
        for j in range(N-2):
            for x in range(3):
                if arr[i+x][j:j+3] != pattern[x]:
                    break
            else:
                result += 1
    print(result)