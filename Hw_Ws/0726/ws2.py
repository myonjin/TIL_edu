def low_and_up(chr):
    
    count=1
    lap=''
    for i in range(len(chr)):
        if count%2==1:
            count+=1
            lap+=chr[i].lower()


        elif count%2==0:
            count+=1
            lap+=chr[i].upper()


    return lap


print(low_and_up('apple'))
print(low_and_up('banana'))