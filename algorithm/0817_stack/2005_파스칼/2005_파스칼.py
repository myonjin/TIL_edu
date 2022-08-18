import sys
sys.stdin = open('input.txt')

tc=int(input())
for t in range(1,tc+1):
    n=int(input())      #파스칼의 길이
    stc=[]              #출력값 담을 리스트
    for i in range(n):  #길이만큼  반복
        stc_2=[]          #각줄의 리스트
        for j in range(i+1): # 각줄의 길이 1,2,3,4
            if j==0 or j==i: # 양쪽 끝이면 1넣기
                stc_2.append(1)
            else:                   #전줄의 자기 인덱스값-1 + 자기인덱스값
                stc_2.append(stc[i-1][j-1]+stc[i-1][j])
        stc.append(stc_2)

    print(f'#{t}')
    for i in stc:
        print(*i)

