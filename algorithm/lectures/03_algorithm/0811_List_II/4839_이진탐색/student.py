# 이진탐색
import sys
sys.stdin = open('input.txt')

# 이진 검색 함수
def binarySearch(a, N, key):
    start = 1
    end = N
    count = 0
    while start <= end:
        middle = int((start + end)/2)
        count += 1
        # print(middle)
        if middle == key:    # 검색 성공
            return count
        elif middle > key:
            end = middle - 1
        else:
            start = middle + 1

# test case
tc = int(input())

# 아래부터 이진 검색 시작
for t in range(1, tc+1):
    p, pa, pb = map(int, input().split())
    # 검색할 리스트(책) 만들기
    book = []
    for i in range(1, p+1):
        book.append(i)

    # 이제 A와 B를 이진 검색
    num_a = binarySearch(book, p, pa)
    #print(num_a)
    num_b = binarySearch(book, p, pb)
    #print(num_b)

    if num_a > num_b:
        print(f'#{t} B')
    elif num_a < num_b:
        print(f'#{t} A')
    else:
        print(f'#{t} 0')