
dic={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
dic_2={'001101':0,'010011':1,'111011':2,'110001':3,'100011':4,'110111':5,'001011':6,'111101':7,'011001':8,'101111':9}
M=input()
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
i=0
while i<len(output):
    if dic_2.get(output[i:6+i]) or dic_2.get(output[i:6+i])==0:
        print(dic_2.get(output[i:6+i]))
        i+=6
        continue
    i+=1
# B=0
# print(output)
# while B<len(output):
#     A=2+i
#     B=8+i
#     print(output[A:B])
#     if dic_2.get(output[A:B]) or dic_2.get(output[A:B])==0:
#         print(dic_2.get(output[A:B]))
#     i+=6
#0269FAC9A0


