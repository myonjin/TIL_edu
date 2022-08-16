import sys
sys.stdin = open('input.txt')

T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split()) #선길이,찾을단어길이
    sqr=[list(input())for _ in range(N)]
    ans=[]
    #가로 판별식
    for l in range(N): #세로
        for i in range(N-M+1): # 총길이안 문장 길이범위
            pan=0
            for j in range(M//2):
                if sqr[l][i+j] == sqr[l][i+M-1-j]:
                    pan+=1
                if pan==M//2:
                    for k in range(i,i+M):
                        ans.append(sqr[l][k])
    #세로 판별식
    for i in range(N): # 가로 0 부터
        for j in range(N-M+1):
            pan=0
            for l in range(M//2):
                if sqr[j+l][i]==sqr[j+M-1-l][i]:
                    pan+=1
                if pan == M // 2:
                    for k in range(j, j + M):
                        ans.append(sqr[k][i])

    print(f'#{tc} {"".join(ans)}')




# print(word == word[::-1])