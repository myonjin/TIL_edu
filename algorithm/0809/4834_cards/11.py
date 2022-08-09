import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    N = int(input())
    build = list(map(int, input().split()))
    result=0
    height_build = 0
    for i in range(2,N-2): # 빌딩 2부터 N-2 까지
        if build[i]>build[i-2] and build[i]>build[i-1] and build[i]>build[i+1] and build[i]>build[i+2]:
            # 구하고자하는 빌딩이 제일 클때
            height_build=0
            # 기본값 0으로
            for j in range(5): # 0,1,2,3,4 2일땐 continue 본체이므로
                # build[i+j-2]   -2 -1 0 1 2
                if j==2: # build[i] 값이므로 스킵
                    continue
                elif height_build<build[i+j-2]:
                    height_build=build[i+j-2] # 조망권을 차지하는 빌딩중 제일큰값

                height_build
            result += build[i]-height_build # 본체 - 조망권빌딩중 제일큰값
    print(f"#{tc} {result}")