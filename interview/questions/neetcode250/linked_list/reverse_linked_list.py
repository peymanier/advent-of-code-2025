from interview.structures.linked_list import build_linked_list, print_linked_list


def reverse_linked_list_rec(head):
    prev = None

    def reverse(node):
        if not node:
            return

        nonlocal prev
        nex = node.next
        node.next = prev
        prev = node

        reverse(nex)

    reverse(head)
    return prev


def reverse_linked_list_rec_alt(head):
    if not head:
        return None

    new_head = head
    if head.next:
        new_head = reverse_linked_list_rec_alt(head.next)
        head.next.next = head

    head.next = None
    return new_head


def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex

    return prev


def main():
    head = build_linked_list([1, 2, 3, 4, 5])
    result = reverse_linked_list(head)
    print_linked_list(result)

    head = build_linked_list([1, 2, 3, 4, 5])
    result = reverse_linked_list_rec(head)
    print_linked_list(result)

    head = build_linked_list([1, 2, 3, 4, 5])
    result = reverse_linked_list_rec_alt(head)
    print_linked_list(result)


if __name__ == "__main__":
    main()
