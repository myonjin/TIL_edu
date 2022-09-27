def f(i,k):
    if i == k:
        print(p)



    else:
        for j in range(i,k):
            p[i],p[j] = p[j], p[i]
            f(i+1,k)
            p[i],p[j] = p[j], p[i]   #원상복귀
p=[1,2,3]
f(0,3)