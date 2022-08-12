import sys
sys.stdin = open('input.txt', encoding='utf-8')

def bruteForce(pattern, target):
    count = 0
    for i in range(len(target) - len(pattern) + 1):
        for j in range(len(pattern)):
            # 두 값이 다른 경우가 나올때까지 계속 돌린다
            if pattern[j] != target[i+j]:
                break
        else: # for문 돌동안 break안하고 다 맞았으면
            count += 1
    return count

for _ in range(10):
    tc = int(input())
    p = input()
    T = input()
    print(bruteForce(p, T))