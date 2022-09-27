import sys
sys.stdin = open('input.txt')
def merge(arr):
    global result
    # 더 이상 쪼갤 수 없는 상황이 올때까지 쪼갠다.
    if len(arr) == 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge(left)
    right = merge(right)
    # print(left,right)

    if left[-1] > right[-1]:
        result += 1
    # 좌,우 값 비교를 위한 인덱스
    # 내가 지금 조사한 그 값을 원본 배열의 어디에 넣을지도 같이 초기화
    l_idx, r_idx = 0, 0
    k = 0
    # 좌, 우 인덱스 들이, 좌, 우 배열들을 넘어서기 직전까지

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            arr[k] = left[l_idx]
            l_idx += 1
        else:
            arr[k] = right[r_idx]
            r_idx += 1
        k += 1
    #인덱스가 넘어갈때
    if l_idx >= len(left):
        arr[k:] = right[r_idx:]
    if r_idx >= len(right):
        arr[k:] = left[l_idx:]
    return arr


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    nums = list(map(int,input().split()))

    #병합 과정에서 왼쪽끝이 오른쪽 끝보다 큰 경우의수
    result=0
    # 병합 정렬을 끝낸 리스트
    ans =merge(nums)
    print(f'#{tc} {ans[N//2]} {result}')