t = int(input())
for tc in range(1, t + 1):
    s = list(map(str, input().split()))

    stack = []
    for n in s:
        if n == '.':
            if len(stack) == 1:
                print("#" + str(tc), stack.pop())
            else:
                print("#" + str(tc), 'error')
        elif n.isdigit():
            stack.append(n)
        else:
            if len(stack) < 2:
                print("#" + str(tc), 'error')
                break
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if str(a).isalpha() or str(b).isalpha():
                    print("#" + str(tc), 'error')
                    break
                elif n == '+':
                    stack.append(a + b)
                elif n == '-':
                    stack.append(a - b)
                elif n == '/':
                    stack.append(int(a // b))
                elif n == '*':
                    stack.append(a * b)
