class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    # def enqueue2(self, item):
    #     self.items.insert(0, item)

    def dequeue(self):
        if not self.items:
            return None

        return self.items.pop(0)

    # def dequeue2(self):
    #     if not self.items:
    #         return None
    #
    #     return self.items.pop()
    #
    # def dequeue3(self):
    #     if not self.items:
    #         return None
    #
    #     item = self.items[-1]
    #     del self.items[-1]
    #     return item

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.items:
            return None

        return self.items[0]


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def add_to_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head = node

    def add_to_tail(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def remove_from_head(self):
        if not self.head:
            return None

        head = self.head
        self.head = head.next
        if not self.head:
            self.tail = None

        head.next = None
        return head


if __name__ == "__main__":
    ll = QueueLinkedList()
    ll.add_to_tail(Node(5))
    ll.add_to_tail(Node(6))
    ll.add_to_head(Node(0))
    ll.add_to_head(Node(-1))
    ll.add_to_tail(Node(7))
    ll.remove_from_head()

    for node in ll:
        print(node.val)
