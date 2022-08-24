from collections import deque
from pprint import pprint

# double ended queue
# q = []
q = deque()
pprint(dir(q))


q.append('A')
q.append('B')
print(q)
q.appendleft('C')
print(q)

print(q.pop())
print(q.popleft())