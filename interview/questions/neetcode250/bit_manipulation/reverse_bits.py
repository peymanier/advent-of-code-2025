import unittest
from collections import deque

# def get_bits(n: int) -> list[int]:
#     que = deque()
#     while n:
#         que.appendleft(n % 2)
#         n >>= 1
#
#     return list(que)


# def get_bits(n: int) -> list[int]:
#     que = deque()
#     while n:
#         que.appendleft(n & 1)
#         n >>= 1
#
#     return list(que)
#
#
# def reverse_bits(n: int) -> int:
#     result = [0 for _ in range(32)]
#     num_bits = get_bits(n)
#
#     idx = 0
#     for i in range(len(num_bits) - 1, -1, -1):
#         result[idx] = num_bits[i]
#         idx += 1
#
#     return int("".join([str(b) for b in result]), 2)


def reverse_bits(n: int) -> int:
    result = 0
    for i in range(32):
        bit = (n >> i) & 1
        result |= bit << (31 - i)

    return result


class Test(unittest.TestCase):
    def test1(self):
        n = 43261596
        got = reverse_bits(n)
        expected = 964176192
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
