class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def build_linked_list(elements: list) -> Node:
    nodes = []
    for elem in elements:
        nodes.append(Node(elem))

    for i in range(1, len(nodes)):
        curr = nodes[i]
        prev = nodes[i - 1]
        prev.next = curr

    return nodes[0]


def print_linked_list(head: Node):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next

    print()


class LinkedList:
    def __init__(self, node: Node | None = None):
        self.curr = node
        self.head = node

    # def __iter__(self):
    #     curr = self.head
    #     while curr:
    #         yield curr
    #         curr = curr.next

    def __iter__(self):
        return self

    def __next__(self):
        val = self.curr
        if not self.curr:
            raise StopIteration("end of linked list")

        self.curr = self.curr.next
        return val

    def add_to_tail(self, node: Node):
        if not self.head:
            self.head = node
            self.curr = node
            return

        prev = None
        curr = self.head
        while curr:
            prev = curr
            curr = curr.next

        if prev:
            prev.next = node


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4])
    ll = LinkedList(head)
    ll.add_to_tail(Node(5))
    ll.add_to_tail(Node(6))

    for node in ll:
        print(node.val)
