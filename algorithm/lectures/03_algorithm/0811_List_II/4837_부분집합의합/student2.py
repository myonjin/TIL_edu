from pprint import pprint

def make_subset(B, N):
    if N == 1:
        for i in range(len(B)):
            print(B[i], end=' ')


def sum_subset(A, N, M):       # N : 부분집합의 크기, M : 범위 시작값
    subset = []

    if N == 1:
        for i in range(M, len(A)):
            subset += [A[i]]
        return subset

    else:
        for i in range(M, len(A)-N+1):
            subset += [A[i]]
            subset += [sum_subset(A, N-1, i+1)]

    return subset


A = [1, 2, 3, 4, 5]

N = int(input())

pprint(sum_subset(A, N, 0))