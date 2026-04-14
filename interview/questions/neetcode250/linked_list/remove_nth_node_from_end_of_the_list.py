import unittest

from interview.structures.linked_list import Node, build_linked_list, get_linked_list


def remove_nth_node(head: Node, n: int) -> Node:
    curr = head
    right = head
    for _ in range(n):
        right = right.next

    while right.next:
        curr = curr.next
        right = right.next

    curr.next = curr.next.next
    return head


class Test(unittest.TestCase):
    def test1(self):
        head = build_linked_list([1, 2, 3, 4, 5])
        n = 2
        got = remove_nth_node(head, n)
        expected = [1, 2, 3, 5]
        self.assertEqual(expected, get_linked_list(got))


if __name__ == "__main__":
    unittest.main()
