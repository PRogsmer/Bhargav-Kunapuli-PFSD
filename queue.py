class queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

q = queue()
q.enqueue(10)
q.enqueue(30)
q.enqueue(70)
q.size()
print((q.size()))
q.dequeue()
print(q.peek())