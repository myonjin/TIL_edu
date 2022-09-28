def find_set(n):
    if n==p[n]:
        return n
    else:
        return find_set(p[n])

def union(a,b):
    p[find_set(b)]=find_set(a)

p=[0,1,2,2,4,4]
union(2,4)
print(find_set(3))
print(p)
