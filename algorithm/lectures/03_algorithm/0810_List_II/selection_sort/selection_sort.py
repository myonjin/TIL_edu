def selection_sort(arr, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [93, 3, 61, 52, 81, 6, 91]
N = len(arr)

selection_sort(arr,N)
print(arr)