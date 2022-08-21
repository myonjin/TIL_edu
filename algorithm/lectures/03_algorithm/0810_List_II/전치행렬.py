from pprint import pprint

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# for i in range(3):
#     print(*arr[i])
#
# for i in range(3):
#     for j in range(i+1, 3):
#         arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
# print('='*30)
# for i in range(3):
#     print(*arr[i])
arr = ['123', '456', '789']
arr = list(zip(*arr))
for i in range(3):
    print(*arr[i])