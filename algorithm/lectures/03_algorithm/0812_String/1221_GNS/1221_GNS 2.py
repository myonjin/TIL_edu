import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1):
    tc, str_len = map(str, input().split())
    numbers = input().split()
    new_numbers = []
    result = []
    
    # 문자 -> 숫자 & 숫자 -> 문자 조합
    str_to_number = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    number_to_str = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
    
    # 문자 -> 숫자
    # 반복을 돌면서
    for number in numbers:
        # 문자를 숫자로 바꿔서 리스트에 추가
        new_numbers.append(str_to_number[number])
    
    # 숫자 리스트 정렬
    # new_numbers.sort()
    for i in range(len(new_numbers)-1, 0, -1):
        for j in range(i):
            if new_numbers[j] > new_numbers[j+1]:
                new_numbers[j], new_numbers[j+1] = new_numbers[j+1], new_numbers[j]
    
    # (정렬된) 숫자 -> 문자
    for number in new_numbers:
        result.append(number_to_str[number])
    
    # 출력
    print(f'{tc}')
    print(f'{" ".join(result)}')