a = [1, 2, 3, 4, 5]
b = a
a[2] = 5
print(a)
print(b)

# a와 b는 같은 주소 [1,2,3,4,5]를 공유하고있는것
# 바뀌면 다 바뀐다