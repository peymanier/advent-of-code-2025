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
