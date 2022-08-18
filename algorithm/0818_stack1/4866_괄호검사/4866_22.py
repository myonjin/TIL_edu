import sys
sys.stdin = open('input.txt')

t=int(input())
for tc in range(1,t+1):
    s=input()
    stack=[]
    for i in s:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            elif not stack:
                stack.append(i)
                break
            elif stack and stack[-1] == '{':
                stack.append(i)
        elif i == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            elif not stack:
                stack.append(i)
                break
            elif stack and stack[-1] == '(':
                stack.append(i)

    if len(stack)==0:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')