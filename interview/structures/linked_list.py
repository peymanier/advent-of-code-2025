class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}"


def build_linked_list(elements: list) -> Node:
    nodes = []
    for elem in elements:
        nodes.append(Node(elem))

    for i in range(1, len(nodes)):
        curr = nodes[i]
        prev = nodes[i - 1]
        prev.next = curr

    return nodes[0]


def get_linked_list(head: Node) -> list:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next

    return result


def print_linked_list(head: Node):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next

    print()


END = object()


class LinkedList:
    def __init__(self, node: Node | None = None):
        self.head = node
        self.curr = None

    # def __iter__(self):
    #     curr = self.head
    #     while curr:
    #         yield curr
    #         curr = curr.next

    def __iter__(self):
        return self

    def __next__(self):
        if not self.curr:
            self.curr = self.head

        curr = self.curr
        if self.curr == END:
            raise StopIteration("end of linked list")

        if self.curr.next:
            self.curr = self.curr.next
        else:
            self.curr = END

        return curr

    def add_to_tail(self, node: Node):
        if not self.head:
            self.head = node
            return

        prev = None
        curr = self.head
        while curr:
            prev = curr
            curr = curr.next

        if prev:
            prev.next = node

    def add_to_head(self, node):
        if not self.head:
            self.head = node
            return

        node.next = self.head
        self.head = node


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4])
    ll = LinkedList(head)
    ll.add_to_tail(Node(5))
    ll.add_to_tail(Node(6))
    ll.add_to_head(Node(0))
    ll.add_to_head(Node(-1))

    for node in ll:
        print(node.val)
