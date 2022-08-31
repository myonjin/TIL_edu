a=[[1],[2,3],[4,5,6],[7,8,9,10]]
result=0
for i in a:
    for j in a[i]:
        result+=a[i][j]

print(result)