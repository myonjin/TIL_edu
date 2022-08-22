from pprint import pprint
import sys
sys.stdin = open('input.txt')
t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    arr_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    main_list = []
    for i in range(1, 1 << 12):
        sub_list = []
        #j는 arr_a의 인덱스이므로 0부터 조회해야
        #모든 요소 포함 여부 확인 가능
        for j in range(12):
            if i & (1 << j):
                # print(arr_a[j], end=' ')
                sub_list.append(arr_a[j])
        # print()
        # print(sub_list)
        main_list.append(sub_list)

    # pprint(main_list)

    # #길이 조건에 맞는 부분집합을 담은 함수 len_list
    len_list = []
    for i in main_list:
        if len(i) == n:
            len_list.append(i)


    # print(len_list)
    #
    total = 0
    count = 0
    #부분집합의 합을 반환하는 total
    #그 total이 문제의 k와 같다는 조건이 성립할 때 증가하는 count
    for i in len_list:
        total = 0
        for j in i:
            total += j

        if total == k:
            count += 1


    print(f'#{tc} {count}')