
salt_per=[] #소금 퍼센트
salt_water=[] #소금물
salt=[0] #소금
i=0
result=0
t_salt_w=0
t_salt_p=0
t_salt_s=0
while i<5:
    
    a=input(f'{i+1}.소금물의 농도(%)와 소금물의 양(g)를 입력하십시오: ')
    if a=='Done':
        break
    
    salt_per.append(int(a[:a.find('%')]))   #=[1]
    salt_water+=[int(a[a.find(' ')+1:a.find('g')])] #= [400]
    
    print(salt_per)
    print(salt_water)

    salt.append(salt_water[i]/100*salt_per[i])

result=sum(salt)/sum(salt_per)

print(result)



# 소금물 = 소금물 끼리 더해줌 

# 소금 = 소금물/100*x%

# 출력에시= 소금/소금물


