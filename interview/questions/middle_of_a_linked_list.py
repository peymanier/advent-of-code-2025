from interview.structures.linked_list import (
    Node,
    build_linked_list,
    print_linked_list,
)


def middle_of_linked_list(head: Node) -> int:
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val


def main():
    head = build_linked_list([0, 1, 2, 3, 4])
    print_linked_list(head)

    result = middle_of_linked_list(head)
    print(result)

    head = build_linked_list([0, 1, 2, 3, 4, 5])
    print_linked_list(head)

    result = middle_of_linked_list(head)
    print(result)


if __name__ == "__main__":
    main()
