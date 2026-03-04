class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def enqueue2(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.items:
            return None

        return self.items.pop(0)

    def dequeue2(self):
        if not self.items:
            return None

        return self.items.pop()

    def dequeue3(self):
        if not self.items:
            return None

        item = self.items[-1]
        del self.items[-1]
        return item

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.items:
            return None

        return self.items[0]
