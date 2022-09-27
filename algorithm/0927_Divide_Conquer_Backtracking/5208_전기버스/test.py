
N=10
arr=[2 ,1, 3, 2, 2, 5, 4 ,2 ,1]
print(N, arr)
n = len(arr)
bit = [1,0,1,0,0,1,0,0,0]
bit[0] = 1
min_charge = 999999
charge = 0
for i in range(n):
    if bit[i] == 1 and bit.count(1) - 1 <= min_charge:
        charge += arr[i]
        if charge >= N:
            min_charge = bit.count(1) - 1
    else:
        continue
print(min_charge)