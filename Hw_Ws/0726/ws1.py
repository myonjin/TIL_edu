def duplicated_letters(chr):
    
    result=[]
    for i in chr:
        if chr.count(i)>1:
            if result.count(i)>=1:
                pass

            else:
                result.append(i)


            

    return result
    

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))