from interview.structures.linked_list import build_linked_list, print_linked_list, Node


def merge_two_sorted_lists(head1, head2):
    dummy = Node(None)
    curr = dummy
    curr1 = head1
    curr2 = head2
    while curr1 and curr2:
        if curr1.val <= curr2.val:
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next

        curr = curr.next

    if curr1:
        curr.next = curr1

    if curr2:
        curr.next = curr2

    return dummy.next


def main():
    head1 = build_linked_list([1, 2, 4])
    head2 = build_linked_list([1, 3, 4])
    result = merge_two_sorted_lists(head1, head2)
    print_linked_list(result)

    head1 = build_linked_list([1, 2, 4])
    head2 = build_linked_list([1, 3, 4, 5, 6, 7])
    result = merge_two_sorted_lists(head1, head2)
    print_linked_list(result)


if __name__ == "__main__":
    main()
