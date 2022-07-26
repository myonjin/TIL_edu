from re import I


salt_per=[] #소금 퍼센트
salt_water=0 #소금물
salt=[] #소금
i=0
result=0
t_salt_w=0
t_salt_p=0
t_salt_s=0
while i<5:
    i +=1
    a=input(f'{i}.소금물의 농도(%)와 소금물의 양(g)를 입력하십시오: ')
    if a=='Done':
        break
    
    salt_per.append(int(a[:a.find('%')]))   #=[1]
    salt_water=int(a[a.find(' ')+1:a.find('g')]) #= 400
    t_salt_w+=int(salt_water[i-1])
    t_salt_s+=int(salt_water[i-1])
    salt=salt_water/100*salt_per[i-1]

print(salt_per)
print(salt_water)
s_w=sum(salt_water)
result=salt/s_w

# 소금물 = 소금물 끼리 더해줌 

# 소금 = 소금물/100*x%

# 출력에시= 소금/소금물


