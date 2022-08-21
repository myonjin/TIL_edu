arr = ['Fish', 'And', 'Chips']
N = len(arr)

for i in range(1<<N):
    tmp = []
    for j in range(N):
        # i : 1 => [0, 0, 0, 1]
        # j : 0 => 1 >> j : [0, 0, 0, 1]
        # j : 1 => 1 >> j : [0, 0, 1, 0]
        if i & (1<<j):
            print(f'{i}번째 경우의 수 {bin(i)[2:]:0>4}')
            print(f'{j}번째 요소 비교 {bin(1<<j)[2:]:0>4}')
            # tmp.append(arr[j])
            print(arr[j], end=' ')
            print()
    # if len(tmp) == 2:
    #     print(tmp)
    print()