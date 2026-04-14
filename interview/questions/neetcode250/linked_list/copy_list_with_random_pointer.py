from interview.structures.linked_list import build_linked_list


class Node:
    def __init__(self, val, nxt=None, rand=None):
        self.val = val
        self.next = nxt
        self.rand = rand

    def __str__(self):
        return f"{self.val}"


def deep_copy_linked_list(head: Node) -> Node:
    old_to_new = {None: None}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    curr = head
    while curr:
        old_to_new[curr].next = old_to_new[curr.next]
        old_to_new[curr].rand = old_to_new[curr.rand]
        curr = curr.next

    return old_to_new[head]


def main():
    head = build_linked_list([7, 13, 11, 10, 1])
    head.rand = None
    head.next.rand = head
    head.next.next.rand = head.next.next.next.next
    head.next.next.next.rand = head.next.next
    head.next.next.next.next.rand = head

    curr = head
    while curr:
        print(curr.val, curr.rand, sep="-", end=" ")
        curr = curr.next

    print()

    new_head = deep_copy_linked_list(head)
    curr = new_head
    while curr:
        print(curr.val, curr.rand, sep="-", end=" ")
        curr = curr.next

    print()


if __name__ == "__main__":
    main()
