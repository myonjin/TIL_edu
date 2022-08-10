import sys
sys.stdin = open('input.txt')
TC = int(input())
#K=이동가능 수 N=종점번호 M:충전기충전정류장수
for tc in range(1,TC+1):
    num=[]
    K, N, M =list(map(int,input().split()))
    num=list(map(int, input().split()))
    jung=[0]*(N+1)
    count=-1

    for i in num:
        jung[i]+=1 # 여기까지 기본 세팅
    if num[0]>K or N-num[-1]>K:
        count=0
    for i in range(len(num)-1):
        if num[i+1]-num[i]>K:
            count=0

    if count == -1:
        # 카운트 0으로 초기화
        count = 0
        # 커서 0에서 출발
        cur = 0
        while cur < N:
            # 현재 커서와 도착지 사이 간격이 K 이하일 때,
            # 주유소 경유 없이 도착 가능하므로 break
            if N - cur <= K:
                break

            # 현재 커서~K까지 간격을 역순 탐색하며
            # 구간 내 가장 idx 큰 주유소 탐색 후 count
            for b in range(K + cur, cur, -1):
                if b in num:
                    cur = b
                    count += 1
                    # print(cur, count)
                    break

    print(f"#{tc} {count}")



