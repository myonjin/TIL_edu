import sys
sys.stdin = open('input.txt')

N = int(input())

for tc in range(1, N+1):
    c = [0]*12 # 각 인데스 번호별 숫자 갯수를 담는다
    num = int(input())
    for i in range(6):
        # 111456 이면 뒤에서 부터 나머지 쌓인다
        c[num % 10] += 1
        num //= 10
    i = 0
    tri = 0
    run = 0
    while i<10: # i 0에서부터 하나씩 이게 맞는지 확인
        if c[i] >=3:
            c[i] -=3
            tri +=1
            continue # tri인지 확인
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2]>=1:
            c[i]-=1
            c[i+1]-=1
            c[i+2] -=1
            run+=1
            continue #연속된 숫자인지 확인
        i+=1
    if tri+run == 2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

