import sys
sys.stdin = open('input.txt')

def recur(idx, arr):
    global result
    # 전체를 돌았을 때
    if idx == 12:
        # 해당 경우의 수의 요소 개수가 r개와 같다면
        if len(arr) == N and sum(arr) == K:
            result += 1
        return
    # 자기 자신을 포함시킬 경우
    arr.append(nums[idx])
    recur(idx+1, arr)
    # 자기 자신을 포함시키지 않을 경우
    arr.pop()
    recur(idx+1, arr)

T = int(input())

for tc in range(1, T+1):
    # 만들 조합의 수 N
    # 모든 수의 합 K
    N, K = map(int, input().split())

    # 숫자 목록
    nums = list(range(1, 13))
    result = 0
    recur(0, [])
    print(result)