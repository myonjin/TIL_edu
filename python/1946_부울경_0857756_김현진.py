for a in range(1, int(input())+1):
    N = int(input())
    lis = []
    words = ''
    for _ in range(N):
        lis.append(input().split())
    for i in range(N):
        words += lis[i][0] * int(lis[i][1])
    print('#{}'.format(a))
    cnt = 0
    for w in words:
        print(w, end='')
        cnt += 1
        if cnt == 10:
            print()
            cnt = 0
    print()