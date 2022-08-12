import sys
sys.stdin = open('input.txt', encoding='utf-8')
tc=int(input())
for tc in range(1,tc+1):
    number,a=input().split()
    leng=int(a)
    str_li=list(input().split()) # 입력값
    num_str={0:"ZRO",1:"ONE",2:"TWO",3:"THR",4:"FOR",5:"FIV", 6:"SIX", 7:"SVN", 8:"EGT", 9:"NIN"}
    str_num={"ZRO":0,"ONE":1,"TWO":2,"THR":3,"FOR":4,"FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    result_1=[]
    result_2=[]
    for i in str_li:
        result_1.append(str_num.get(i))
    result_1.sort()
    for i in result_1:
        result_2.append(num_str.get(i))
    print(f"#{tc}")
    print(' '.join(result_2))