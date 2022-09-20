import sys
sys.stdin = open('input.txt')
dic_2={
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9
}
T=int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split()) #배열 세로크기(i), 배열 가로크기(j)
    result=[]
    final=0
    for _ in range(N):
        output=input()
        arr=list(map(int,output))
        if sum(arr)>1:
            i=0
            while i < len(output):
                if dic_2.get(output[i: 7 + i]) or dic_2.get(output[i: 7 + i]) == 0:
                    # print(dic_2.get(output[i:7 + i]))
                    result.append(dic_2.get(output[i:7 + i]))
                    i += 7
                    if len(result)==8:
                        break
                    continue
                elif len(result)>=1:
                    if not dic_2.get(output[i: 7 + i]) or dic_2.get(output[i: 7 + i]) == 0:
                        result=[]
                        i-=6
                i += 1
        else:
            continue
    final=(result[0]+result[2]+result[4]+result[6])*3+result[1]+result[3]+result[5]+result[7]
    if final%10==0:
        print(f'#{tc} {result[0]+result[2]+result[4]+result[6]+result[1]+result[3]+result[5]+result[7]}')
    else:
        print(f'#{tc} 0')

