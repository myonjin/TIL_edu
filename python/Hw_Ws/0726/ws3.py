def lonely(list):

    result=[list[0]]
    for i in range(1,len(list)):
        if list[i]!=list[i-1]:
            result.append(list[i])
        else:
            pass




    return result


print(lonely([1,1,3,3,0,1,1]))
print(lonely([4,4,4,3,3]))


def lonely(numbers):
    result = []
    for num in numbers:
        if not result:
            result.append(num)
        else:
            if result[-1] != num:
                result.append(num)
    return result

def lonely(numbers):
    result = [numbers[0]] # result = [1]
    for num in numbers:
        if result[-1] != num:
            result.append(num)
    return result