import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1):
    tc, n = input().split()
    words = input().split()
    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    result = ''

    for number in numbers:
        for word in words:
            if word == number:
                result += word + ' '

    print(tc)
    print(result)