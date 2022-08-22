class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
            return self.items == []

    def push(self,item):
            self.items.append(item)

    def pop(self):
            return self.items.pop()

    def peek(self):
            return self.items[len(self.items)-1]

    def size(self):
            return len(self.items)

s = stack()
s.push(10)
s.push(20)
s.push(30)
s.size()
print(s.size())
s.is_empty()
print(s.is_empty())

def evenorodd(n):
    if n%2 == 0:
        print("IT IS ODD NUMBER")
    else:
        print("IT IS EVEN NUMBER")
