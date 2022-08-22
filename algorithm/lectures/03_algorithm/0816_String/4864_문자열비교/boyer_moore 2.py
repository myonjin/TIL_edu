import sys
sys.stdin = open('input.txt')

def process(pattern):
    M = len(pattern)

    # skip 할 딕셔너리
    PI = dict()

    # (M - i - 1)만큼 스킵
        # 마지막 단어는 패턴 길이만큼 스킵 할 것이기 떄문에
        # 스킵 길이 조사 X
    for i in range(M-1):
        PI[pattern[i]] = M - (1+i)
    return PI

def boyer_moore(pattern, target):
    PI = process(pattern)

    M = len(pattern)

    # index 기준 조회
    i = 0

    # i <= 전체 target 길이 - 패턴 길이
    while i <= len(target) - M:
        # pattern의 index == M - 1
        j = M - 1

        # 내가 현재 패턴이랑 비교 해야하는
        # target의 index
        K = i + (M-1)

        while j >= 0 and pattern[j] == target[K]:
            j -= 1
            K -= 1

        if j == -1:
            return 1

        i += PI.get(target[i + M -1], M)
    return 0



T = int(input())

for tc in range(1, T+1):
    pattern, target = input(), input()
    result = boyer_moore(pattern, target)
    print(f'#{tc} {result}')