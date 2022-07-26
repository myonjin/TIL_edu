def count_blood(type):
    result = {}
    for blood in type:
        if result.get(blood):
            result[blood] +=1
        else:
            result[blood]=1
    return result

def count_blood(type):
    result = {}
    for blood in type:
        result[blood]=result.get(blood,0) + 1
    return result

print(count_blood(['A','B','A','O','AB','O','A','B','O','B','AB']))
