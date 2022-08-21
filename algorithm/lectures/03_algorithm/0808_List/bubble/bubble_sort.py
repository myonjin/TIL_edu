def bubble_sort(arr): # 정렬할 리스트, N 원소 수
    # 1. n-1 번째 부터 조사를 해나갈 거야.
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            # 이전 요소가 이후 요소보다 크면
            # 교환을 해야지 버블 소트가 되겠자
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
    return arr

numbers = [9, 13, 64, 62, 3]

print(bubble_sort(numbers))
