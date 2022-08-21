import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = input(), input()
    result = 0

    # N에서 중복 제거 (어차피 가장 많은 문자를 찾아야하니)
    for char in set(N):
        # 문자 카운트
        count = 0
        for word in M:
            if char == word:
                count += 1

        # 최댓값 갱신
        if count > result:
            result = count

    print(f'#{tc} {result}')