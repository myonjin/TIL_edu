a=[[1],[2,3],[4,5,6],[7,8,9,10]]
result=0
for i in a:
    for j in a[i]:
        result+=a[i][j]

print(result)


# 00 10 11 20 21 22 30 31 32 33