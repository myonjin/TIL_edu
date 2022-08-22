import sys
sys.stdin = open('input.txt')

"""
규칙성 발견 -> 점화식 -> DP 
이전의 연산 결과가 다음 연산의 결과를 도출하는데 중복되는 경우 
이를 활용할 수 있음

1. 점화식 구하기 -> 규칙 찾아 내기
2. 이전에 풀었던 결과를 활용하여 다음 step 구하기 -> DP
"""
T = int(input())

for tc in range(1, T+1):
    # 종이의 길이 단위가 10 / 이를 1의 단위로 바꿔줌
    N = int(input()) // 10

    """
    가로 10 / 20은 계산된 값 활용 - 피보나치랑 같은 구조
    10 -> 1가지
    20 -> 3가지
    30 -> 5가지 
    40 -> 11가지 
    50 -> 21가지
    ...
    """
    papers = [1, 3]

    # i-2 + i-1 -> i (최종적으로 append되는 값)
    for i in range(2, N):
        """
        점화식 -> f(N) = f(N-1) + f(N-2)*2
        """
        papers.append(papers[i-1] + (2 * papers[i-2]))

    result = papers[-1]

    print(f'#{tc} {result}')