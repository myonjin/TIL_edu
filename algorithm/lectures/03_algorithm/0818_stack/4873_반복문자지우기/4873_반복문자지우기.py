import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    stack = []
    word = input()

    # chars의 원소를 stack에 넣음
    for char in word:
        # stack이 비었으면
        if not stack:
            stack.append(char)
        # stack의 길이가 0이 아니면
        # 스택의 가장 뒤 원소가 char랑 같으면 중복되므로 삭제
        elif stack[-1] == char:
            stack.pop()
        # 아니라면 append
        else:
            stack.append(char)
    result = len(stack)

    print(f'#{tc} {result}')