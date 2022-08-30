import sys
sys.stdin = open('input.txt')

def find_ways_len(x, y):
    di = [1, 0, 0]  # 하 좌 우
    dj = [0, -1, 1]
    d = 0  # 처음 방향 아래로
    cnt = 0

    while True:
        x += di[d]
        y += dj[d]
        cnt += 1
        if x == 99:
            break
        if d == 0:
            if 0 <= y + dj[1] < 100 and ladder[x + di[1]][y + dj[1]] == 1:
                d = 1
            elif 0 <= y + dj[2] < 100 and ladder[x + di[2]][y + dj[2]] == 1:
                d = 2
        else:
            if 0 <= x + di[0] < 100 and ladder[x + di[0]][y + dj[0]] == 1:
                d = 0

    return cnt


for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for i in range(100)]
    result = []

    for i in range(100):
        if ladder[0][i] == 1:
            result.append((find_ways_len(0, i), i))

    result.sort()

    print(f'#{tc} {result[0][1]}')