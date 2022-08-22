import sys
sys.stdin = open('input.txt', encoding='utf-8')

def bruteForce(pattern, target):
    # 현재 조사 대상인 각 idx 초기화
    p_idx, t_idx = 0, 0
    # 패턴이 몇번 나오느냐
    count = 0
    while t_idx < len(target):
        # 조사 대상을 변수에 담아서 사용
        t = target[t_idx]
        p = pattern[p_idx]

        # 두 값이 서로 다를때
        if t != p:
            t_idx = t_idx - p_idx
            p_idx = -1

        t_idx += 1
        p_idx += 1

        # 만약 모든 패턴 조사가 다 끝났다면
        if p_idx == len(pattern):
            # 패턴이 한번 일치한다
            count += 1
            p_idx = 0
    return count


for _ in range(10):
    tc = int(input())
    P = input()
    T = input()

    result = bruteForce(P, T)
    print(f'#{tc} {result}')
