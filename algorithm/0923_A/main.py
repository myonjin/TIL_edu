from collections import deque
a=deque()
a.append([0,0])
i,j=a.popleft()
que=deque([0,0])
while que:
    print(que)
    i,j=que.popleft()
    print(i,j)
