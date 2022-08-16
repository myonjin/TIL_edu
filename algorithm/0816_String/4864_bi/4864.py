import sys
sys.stdin = open('input.txt')

T=int(input())

for tc in range(1,T+1):
    pattern = input()
    target = input()
    count=0
    for i in range(len(target) - len(pattern) + 1):
        for j in range(len(pattern)):
            # 두 값이 다른 경우가 나올때까지 계속 돌린다
            if pattern[j] != target[i+j]:
                break
        else: # for문 돌동안 break안하고 다 맞았으면
            count += 1

    print(f"#{tc} {count}")