class Queue:

    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.rear = -1
        self.front = -1

    def enQueue(self, item):
        self.rear += 1
        self.items[self.rear] = item

    def deQueue(self):
        self.front += 1
        return self.items[self.front]

q = Queue(5)
print(q.items)

q.enQueue('A')
q.enQueue('B')
print(q.items)

print('='*30)
print(q.deQueue())
print(q.items)
