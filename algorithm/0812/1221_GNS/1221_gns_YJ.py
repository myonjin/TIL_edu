import sys
sys.stdin = open('input.txt')

#딕셔너리 카운트
T = int(input())
num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for tc in range(1,T+1):
    a,n = input().split()
    n = int(n)
    dic = dict()
    ls = input().split()
    for x in ls:
       if dic.get(x,0) == 0 : dic[x] = 1
       else : dic[x] += 1
    print(a)
    for y in num:
        for i in range(dic[y]):
            print(y, end=' ')
    print()