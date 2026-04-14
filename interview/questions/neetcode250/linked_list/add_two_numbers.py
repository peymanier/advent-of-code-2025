import unittest

from interview.structures.linked_list import Node, build_linked_list, get_linked_list

# def add_two_numbers(head1: Node, head2: Node) -> Node:
#     first = deque()
#     curr = head1
#     while curr:
#         first.appendleft(str(curr.val))
#         curr = curr.next
#
#     second = deque()
#     curr = head2
#     while curr:
#         second.appendleft(str(curr.val))
#         curr = curr.next
#
#     addition = int("".join(first)) + int("".join(second))
#
#     digits = str(addition)
#     result = Node(int(digits[-1]))
#     prev = result
#     for i in range(len(digits) - 2, -1, -1):
#         curr = Node(int(digits[i]))
#         prev.next = curr
#         prev = curr
#
#     return result


def add_two_numbers(head1: Node, head2: Node) -> Node:
    curr1 = head1
    curr2 = head2
    carry = 0
    dummy = Node(None)
    curr = dummy
    while curr1 or curr2 or carry:
        val1 = curr1.val if curr1 else 0
        val2 = curr2.val if curr2 else 0

        num = val1 + val2 + carry
        curr.next = Node(num % 10)

        if num >= 10:
            carry = 1
        else:
            carry = 0

        curr = curr.next
        curr1 = curr1.next if curr1 else None
        curr2 = curr2.next if curr2 else None

    return dummy.next


class Test(unittest.TestCase):
    def test1(self):
        head1 = build_linked_list([2, 4, 3])
        head2 = build_linked_list([5, 6, 4])
        got = add_two_numbers(head1, head2)
        expected = [7, 0, 8]
        self.assertSequenceEqual(expected, get_linked_list(got))

    def test2(self):
        head1 = build_linked_list([2])
        head2 = build_linked_list([5, 6, 4])
        got = add_two_numbers(head1, head2)
        expected = [7, 6, 4]
        self.assertSequenceEqual(expected, get_linked_list(got))

    def test3(self):
        head1 = build_linked_list([2, 4, 3, 3])
        head2 = build_linked_list([5, 6, 4])
        got = add_two_numbers(head1, head2)
        expected = [7, 0, 8, 3]
        self.assertSequenceEqual(expected, get_linked_list(got))

    def test4(self):
        head1 = build_linked_list([7])
        head2 = build_linked_list([8])
        got = add_two_numbers(head1, head2)
        expected = [5, 1]
        self.assertSequenceEqual(expected, get_linked_list(got))


if __name__ == "__main__":
    unittest.main()
