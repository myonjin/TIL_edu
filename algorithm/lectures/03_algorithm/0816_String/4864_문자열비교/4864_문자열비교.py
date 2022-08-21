import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    pattern, target = input(), input()

    # 최종 결괏값
    result = 0
    # 전체 길이 - 패턴 길이 만큼 순회
    for i in range(len(target)-len(pattern)+1):
        # 전체 길이중, 현재 위치부터 패턴길이까지 슬라이싱 한 값이
        # 패턴과 동일 하다면
        tmp = target[i:i+len(pattern)]
        if tmp == pattern:
            # 1로 변환 후 종료
            result = 1
            break

    print(f'#{tc} {result}')