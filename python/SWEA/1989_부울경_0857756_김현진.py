t = int(input())

for a in range(1, t + 1) :
    data = input()
    temp = ''
    for i in range(len(data)-1, -1, -1) :
        temp += data[i]

    if data == temp :
        print('#%d %d' % (a, 1))
    else :
        print('#%d %d' % (a, 0))

    