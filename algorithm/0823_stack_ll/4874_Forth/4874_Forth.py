import sys
sys.stdin = open('input.txt')
T=int(input())
for tc in range(1,T+1):
    word = list(map(str, input().split()))
    stack = []
    # print(word)
    for i in word:
        if i=='.':
            if len(stack)==1:
                print(f'#{tc}',stack.pop())
            else:
                print(f'#{tc} error')
        elif i.isdigit():
            stack.append(i)
        else:
            if len(stack)>1:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                elif i == '/':
                    stack.append(a // b)
            else:
                print(f'#{tc} error')
                break