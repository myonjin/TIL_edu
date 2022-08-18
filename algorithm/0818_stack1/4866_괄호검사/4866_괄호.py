import sys
sys.stdin = open('input.txt')

t=int(input())
for tc in range(1,t+1):
    s=input()
    stack=[]
    for i in s:
        if i == '(' or i == '{':
            stack.append(i)
        elif i== ')'and stack[-1:]==['(']:
            stack.pop()
        elif i=='}' and stack[-1:]==['{']:
            stack.pop()
        elif i in (')','}') and not stack:
            stack.append(i)
            break
    if len(stack)==0:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')