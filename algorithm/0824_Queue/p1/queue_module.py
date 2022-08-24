from queue import Queue

q = Queue()
q.put('A')
q.put('B')
q.put('C')
print(q.queue)
print(q.qsize())

print(q.get())
print(q.get())
print(q.get())
print(q.queue)

# 멀티스레드 프로그래밍
q = Queue(3)
q.put('A')
q.put('B')
q.put('C')
print(q.queue)
q.put('D')