class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None

        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.items:
            return None

        return self.items[-1]
