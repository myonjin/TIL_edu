import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input()

    op = '{('
    cl = '})'
    stack = []

    result = 0
    for char in data:
        if char in op:
            stack.append(char)
        if char in cl:
            if not stack:
                break
            if char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            else:
                break
    else:
        if not stack:
            result = 1
    print(f'#{tc} {result}')