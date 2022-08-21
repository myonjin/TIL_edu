import sys
sys.stdin = open('input.txt')

def is_palindrome(word):
    idx = 0
    while idx + M-1 < len(word):
        pali = word[idx:idx + M]
        if pali == pali[::-1]:
            return pali
        idx += 1
    return False

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    result = ''

    for i in range(N):
        tmp = ''
        for j in range(N):
            tmp += arr[j][i]
        result = is_palindrome(tmp)
        if result:
            break

        result = is_palindrome(arr[i])
        if result:
            break

    print(f'#{tc} {result}')

