import sys
sys.stdin = open('input.txt')
t=int(input())
for tc in range(1,t+1):
    s=input()
    stack=[]
    for i in s:
        if [i]!=stack[-1:] or not stack:
            stack.append(i)
        else:
            stack.pop()

    print(f'#{tc} {len(stack)}')