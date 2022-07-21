
def all_list_sum(scores):          
    for i in range(len(scores)):  # scores의 길이는 8이다.
        sum = 0
    
        for j in range(len(scores[i])):  # 2중리스트의 각 요소에 접근하기 위해
            sum = sum + scores[i][j]
    return sum

print(all_list_sum([[1],[2,3],[4,5,6],[7,8,9,10]]))

