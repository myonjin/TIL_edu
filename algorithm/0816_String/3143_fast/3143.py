import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(1,T+1):
    a, b = list(input().split())
    result = 0
    cnt = 0
    i = 0
    while i < len(a):
        pan=0
        if i+len(b)<=len(a):
            for j in range(len(b)):
                if a[i+j] != b[j]:
                    break
                else:
                    pan+=1
        if pan==len(b):
            i+=len(b)
        else: i+=1

        cnt += 1

    print(f'#{tc} {cnt}')
