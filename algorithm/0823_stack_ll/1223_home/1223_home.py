import sys
sys.stdin = open('input.txt')

for tc in range(1,11):
    num=int(input())
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
    for i in result:
        if i.isdigit():
            stack.append(i)
        else:
            b=int(stack.pop())
            a=int(stack.pop())
            if i=='+':
                stack.append(a+b)
            elif i=='-':
                stack.append(a-b)
            elif i=='*':
                stack.append(a*b)
            elif i=='/':
                stack.append(a//b)
    print(f'#{tc} {stack[0]}')