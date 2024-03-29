import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    word=input()
    stack = []
    result= ''
    for char in word:
        if char in '/*+-':
            if not stack: #스택이 비어있다면
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char in '/*':
                while stack and stack[-1] in '/*':
                    result +=stack.pop()
                stack.append(char)
            elif char in '+-':
                while stack and stack[-1] !='(':
                    result += stack.pop()
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:
            result +=char
    while stack:
        result += stack.pop()
    print(f'#{tc} {result}')