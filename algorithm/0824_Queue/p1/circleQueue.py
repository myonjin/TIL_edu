class Queue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.rear = self.size
        self.front = 0

    def enQueue(self, item):
        if self.isFull():
            print('is Full')
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = item

    def deQueue(self):
        self.front = (self.front + 1) % self.size
        return self.items[self.front]

    def isFull(self):
        return self.front == (self.rear + 1) % self.size

q = Queue(5)
print(q.items)

q.enQueue('A')
q.enQueue('B')
print(q.items)

print('='*30)
print(q.items)

q.enQueue('C')
q.enQueue('D')
print('='*30)
print(q.items)
q.deQueue()

q.enQueue('E')
print('='*30)
print(q.items)

print('='*30)
print(q.rear, q.front)

'''
교수님 방금 원형큐 isFull 부분에서 예를 들어서 0~5 
인덱스 중에 1~4 부분 채우는 동안 deQ 한번도 하지 않고 
enQ 한 번 더해서 5 -> 0 으로 넘어갈때 front랑 rear랑 겹치는데 
그럴때는 인덱스0자리 못채우나요?
'''