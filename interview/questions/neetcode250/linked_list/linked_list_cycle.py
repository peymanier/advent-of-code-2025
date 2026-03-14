from interview.structures.linked_list import build_linked_list


def detect_cycle(head) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def main():
    head = build_linked_list([3, 2, 0, -4])
    curr = head
    while curr.next:
        curr = curr.next

    curr.next = head.next
    result = detect_cycle(head)
    val = True
    print("passed:", result == val, "expected", val, "got", result)

    head = build_linked_list([1, 2, 3, 4])
    result = detect_cycle(head)
    val = False
    print("passed:", result == val, "expected", val, "got", result)


if __name__ == "__main__":
    main()
