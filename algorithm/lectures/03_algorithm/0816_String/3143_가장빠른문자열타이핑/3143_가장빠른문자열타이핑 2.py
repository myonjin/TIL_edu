import sys

sys.stdin = open('input.txt')

T = int(input())

for  tc in range(1, T+1):
    target, pattern = input().split()

    len_t = len(target)
    len_p = len(pattern)

    idx = 0
    cnt = 0

    # i : target에서 돌아다니는 아이
    while idx <= len_t - len_p:
        if target[idx:idx+len_p] != pattern:
            idx += 1
        # 같다면 pattern를 타이핑 한 후 i를 pattern의 길이만큼 넘어감
        else:
            cnt += 1
            idx += len_p

    # target의 길이만큼 기본적으로 타이핑 해야 하고
    # pattern 만큼의 길이를 1번의 타이핑으로 대체하였기 때문에 (len_p - 1)을 cnt만큼 곱해서 빼줌
    result = len_t - cnt * (len_p - 1)
    print(f'#{tc} {result}')