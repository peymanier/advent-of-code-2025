import unittest
from collections import deque

from interview.structures.linked_list import Node, build_linked_list, get_linked_list


def add_two_numbers(head1: Node, head2: Node) -> Node:
    first = deque()
    curr = head1
    while curr:
        first.appendleft(str(curr.val))
        curr = curr.next

    second = deque()
    curr = head2
    while curr:
        second.appendleft(str(curr.val))
        curr = curr.next

    addition = int("".join(first)) + int("".join(second))

    digits = str(addition)
    result = Node(int(digits[-1]))
    prev = result
    for i in range(len(digits) - 2, -1, -1):
        curr = Node(int(digits[i]))
        prev.next = curr
        prev = curr

    return result


class Test(unittest.TestCase):
    def test1(self):
        head1 = build_linked_list([2, 4, 3])
        head2 = build_linked_list([5, 6, 4])
        got = add_two_numbers(head1, head2)
        expected = [7, 0, 8]
        self.assertSequenceEqual(expected, get_linked_list(got))


if __name__ == "__main__":
    unittest.main()
