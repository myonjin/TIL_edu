T=int(input())
dic={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
for tc in range(1,T+1):
    N,M=input().split()
    output=""
    for temp in M:
        if temp.isdigit():
            temp=int(temp)
            for j in range(3,-1,-1):
                if temp & (1 << j):
                    output+= "1"
                else:
                    output+= "0"
        else:
            temp=dic[temp]
            for j in range(3,-1,-1):
                if temp & (1 << j):
                    output+= "1"
                else:
                    output+= "0"
    print(f'#{tc} {output}')