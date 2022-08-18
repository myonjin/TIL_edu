import sys
sys.stdin = open('input.txt')



def solution(s_input):
    stc = []
    for s in s_input:
        if s == '(':
            stc.append(s)
        elif s == ')':
            if len(stc) == 0:
                return -1
            stc.pop()
    if len(stc) != 0:
        return -1

    return 1

tc=int(input())
for t in range(1,tc+1):
    s_input=input()
    print(f'#{t} {solution(s_input)}')