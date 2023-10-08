

class ArrayQueue:
    def __init__(self, capacity):
        self.data = [None] * capacity
        self.first = 0
        self.rear = 0

    def isEmpty(self):
        return self.first == self.rear

    def size(self):
        return (self.rear - self.first) % len(self.data)

    def enqueue(self, item):
        if self.size() == len(self.data):
            self._resize(2 * len(self.data))
        self.data[self.rear] = item
        self.rear = (self.rear + 1) % len(self.data)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        item = self.data[self.first]
        self.data[self.first] = None
        self.first = (self.first + 1) % len(self.data)
        return item

    def first(self):
        if self.isEmpty():
            raise Exception("Queue underflow")
        return self.data[self.first]

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size()):
            new_data[i] = self.data[(self.first + i) % len(self.data)]
        self.data = new_data
        self.first = 0
        self.rear = self.size()

q = ArrayQueue(5)
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())