def get_middle_char(a):
    if len(a)%2==1:
        center=len(a)//2
        return a[center]
    else:
        center=len(a)//2
        return a[center-1:center+1]

print(get_middle_char('ssafy'))      
print(get_middle_char('coding'))
