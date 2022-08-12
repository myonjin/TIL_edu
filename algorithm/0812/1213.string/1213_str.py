import sys
sys.stdin = open('input.txt', encoding='utf-8')

for tc in range(1,11):
    tc = input()
    st = input()
    test = input()
    result=0
    for i in range(len(test)-len(st)+1):
        pan=0
        for j in range(len(st)):
            if st[j]==test[i+j]: # j= 0 1
                pan+=1
        if pan==len(st):
            result += 1
    print(f"#{tc} {result}")