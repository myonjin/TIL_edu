# Built-in 함수 4가지
# len(),list(),print(),max(),min()

odd_list=[]
for i in range(1,50)[::2]:
    
    odd_list+=[i]
print(odd_list)

odd_list=[]
for i in list(range(1,50)[::2]):
    
    odd_list.append(i)
print(odd_list)