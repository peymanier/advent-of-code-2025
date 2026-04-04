import unittest
from collections import deque

# def add_binary(a: str, b: str) -> str:
#     result = deque()
#     carry = 0
#     i = -1
#     while abs(i) - 1 <= max(len(a), len(b)):
#         try:
#             first = int(a[i])
#         except IndexError:
#             first = 0
#
#         try:
#             second = int(b[i])
#         except IndexError:
#             second = 0
#
#         addition = first + second + carry
#         if addition > 1:
#             carry = 1
#         else:
#             carry = 0
#
#         result.appendleft(str(addition % 2))
#         i -= 1
#
#     if result[0] == "0":
#         result.popleft()
#
#     return "".join(result)


def add_binary(a: str, b: str) -> str:
    result = deque()
    carry = 0
    a, b = a[::-1], b[::-1]
    for i in range(max(len(a), len(b))):
        first = int(a[i]) if i < len(a) else 0
        second = int(b[i]) if i < len(b) else 0

        addition = first + second + carry
        if addition > 1:
            carry = 1
        else:
            carry = 0

        result.appendleft(str(addition % 2))
        i += 1

    if carry:
        result.appendleft(str(carry))

    return "".join(result)


class Test(unittest.TestCase):
    def test1(self):
        a = "11"
        b = "1"
        got = add_binary(a, b)
        expected = "100"
        self.assertEqual(expected, got)

    def test2(self):
        a = "1010"
        b = "1011"
        got = add_binary(a, b)
        expected = "10101"
        self.assertEqual(expected, got)

    def test3(self):
        a = "111"
        b = "111"
        got = add_binary(a, b)
        expected = "1110"
        self.assertEqual(expected, got)

    def test4(self):
        a = "10"
        b = "101"
        got = add_binary(a, b)
        expected = "111"
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
