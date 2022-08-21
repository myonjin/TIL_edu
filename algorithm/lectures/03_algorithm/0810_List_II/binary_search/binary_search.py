def binarySearch(arr, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end) // 2
        print(middle, arr[middle])
        if arr[middle] == key:
            return True
        elif arr[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return False

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
N = len(arr)
key = 8
print(binarySearch(arr, N, key))