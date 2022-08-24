import heapq
arr = [(45, 'z'), (17, 'x'), (6,'a'), (100, 'b')]

heapq.heapify(arr)

print(arr)
'''
         6
    17      45
100
'''
heapq.heappush(arr, (4, 't'))
print(arr)

heapq.heappush(arr, (30, 'f'))
print(arr)
'''
        4
    6       30
100   17  45      
'''
print(heapq.heappop(arr))
print(heapq.heappop(arr))
arr.append((-1, 'z'))
print(arr)