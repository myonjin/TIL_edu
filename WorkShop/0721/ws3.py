
def dict_list_sum(value):
    result =0 
    for i in value:
        result += i['age']

    return result


print(dict_list_sum([{'name':'kim', 'age':12}, {'name':'lee', 'age':4}]))