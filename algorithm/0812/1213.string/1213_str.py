import sys
sys.stdin = open('input.txt', encoding='utf-8')

for tc in range(1,11):
    tc = input()
    st = input() # ti
    test = input() #saesaea
    result=0
    for i in range(len(test)-len(st)+1):
            if st[:]==test[i:i+len(st)]: # j= 0 1
                result += 1
    print(f"#{tc} {result}")