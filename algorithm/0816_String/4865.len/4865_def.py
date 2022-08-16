import sys
sys.stdin = open('input.txt')

T=int(input())

for tc in range(1,T+1):
    pattern=input()
    target=input()


    result=0
    max_count=0
    for i in range(len(pattern)):
        count = 0
        for j in range(len(target)):
            if pattern[i] == target[j]:
                count+=1
        if  max_count<=count: max_count=count;





    print(f"#{tc} {max_count}")
