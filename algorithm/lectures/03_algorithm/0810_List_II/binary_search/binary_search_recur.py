def binarySearch(arr, start, end, key):
    if start > end:
        return False
    else:
        middle = (start + end) // 2
        # print(middle, arr[middle])
        if arr[middle] == key:
            return True
        elif arr[middle] > key:
            return binarySearch(arr, start, middle-1, key)
        else:
            return binarySearch(arr,  middle+1, end, key)

arr = [1, 3, 5, 7, 9, 11]
N = len(arr)
key = 3
print(binarySearch(arr, 0, N-1, key))