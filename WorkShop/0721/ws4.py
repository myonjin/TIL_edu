def all_list_sum(a):
    sum = 0
    for i in a:
        for j in i:

            sum += j
    return sum


all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]])
