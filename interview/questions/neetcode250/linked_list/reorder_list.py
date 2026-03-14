from interview.structures.linked_list import build_linked_list, print_linked_list, Node


def reorder_linked_list(head):
    slow = head
    fast = head
    tail = None
    while fast and fast.next:
        tail = slow
        slow = slow.next
        fast = fast.next.next

    tail.next = None

    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    dummy = Node(None)
    curr = dummy
    curr1 = head
    curr2 = prev
    while curr1 and curr2:
        curr.next = curr1
        curr1 = curr1.next

        curr = curr.next

        curr.next = curr2
        curr2 = curr2.next

        curr = curr.next

    return dummy.next


def reorder_linked_list_alt(head):
    vals = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next

    mid = len(vals) // 2
    first_half = vals[:mid]
    second_half_reversed = vals[-1 : mid - 1 : -1]

    result = []
    i = 0
    j = 0
    while i < len(first_half) and j < len(second_half_reversed):
        result.append(first_half[i])
        i += 1
        result.append(second_half_reversed[j])
        j += 1

    while i < len(first_half):
        result.append(first_half[i])
        i += 1

    while j < len(second_half_reversed):
        result.append(second_half_reversed[j])
        j += 1

    nodes = [Node(val) for val in result]
    for i in range(1, len(nodes)):
        prev = nodes[i - 1]
        curr = nodes[i]
        prev.next = curr

    return nodes[0]


def main():
    head = build_linked_list([1, 2, 3, 4])
    result = reorder_linked_list(head)
    print_linked_list(result)

    head = build_linked_list([1, 2, 3, 4])
    result = reorder_linked_list_alt(head)
    print_linked_list(result)

    head = build_linked_list([1, 2, 3, 4, 5])
    result = reorder_linked_list(head)
    print_linked_list(result)

    head = build_linked_list([1, 2, 3, 4, 5])
    result = reorder_linked_list_alt(head)
    print_linked_list(result)


if __name__ == "__main__":
    main()
