

def list_del(list):
    result=[list[0]]
    for i in range(1,len(list)):
        if list[i] != list[i-1]:
            
            result.append(list[i])
    return result

print(list_del([1,1,3,3,0,1,1]))




# list_in=[1,1,3,3,0,1,1]

# 오른쪽 값과 같으면 본인을 삭제한다 