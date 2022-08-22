import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    # 1은 N극 2는 S극
    data = [list(map(int, input().split())) for _ in range(n)]
    # print(data)
    # 최종 결과
    cnt = 0

    # 테이블 위에 남아 있는 모든 N, S극 제거하기
    NS = 0
    for i in range(n):
        for j in range(n):
            # 현재 조회 좌표가 1 == N극 이다
            if data[i][j] == 1:
                NS += 1
            if data[i][j] == 2:
                NS += 1

    # 모든 극들 다 사라질 떄 까지
    while NS:
        for x in range(n):
            for y in range(n):
                # N극에 대해서
                if data[x][y] == 1:
                    # 내 다음칸이 테이블을 벗어나면
                    if x+1 == n:
                        # 그 N극은 테이블에서 사라짐
                        data[x][y] = 0
                        NS -= 1
                    # N극 기준으로 다음칸이 S극이다 : 교착상태다
                    elif data[x+1][y] == 2:
                        # 교착상태 + 1
                        cnt += 1
                        # 교착상태로 만들기
                        data[x][y] = 3
                        data[x+1][y] = 3
                        # NS의 개수가 2개 감소
                        NS -= 2
                    # N극이 교착상태를 만났다면
                    elif data[x+1][y] == 3:
                        data[x][y] = 3
                        NS -= 1
                    # 같은 극이면 대기
                    elif data[x+1][y] == 1:
                        continue
                    else:
                        data[x][y] = 0
                        data[x+1][y] = 1
                # S극에 대해서
                if data[x][y] == 2:
                    # 벽 체크
                    if x-1 == -1:
                        data[x][y] = 0
                        NS -= 1
                    # N극이랑 대치
                    elif data[x-1][y] == 1:
                        cnt += 1
                        data[x][y] = 3
                        data[x-1][y] = 3
                        NS -= 2
                    elif data[x-1][y] == 3:
                        data[x][y] = 3
                        NS -= 1
                    elif data[x-1][y] == 2:
                        continue
                    else:
                        data[x-1][y] = 2
                        data[x][y] = 0
    print(cnt)
