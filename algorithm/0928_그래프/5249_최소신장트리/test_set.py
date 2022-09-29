def find_set(n):
    if n==p[n]:
        return n
    else:
        return find_set(p[n])

def union(a,b):
    p[find_set(b)]=find_set(a)

p=[0,1,2,3]
union(1,2)
union(3,1)
print(find_set(3))
print(p)
