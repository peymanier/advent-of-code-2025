import math
import unittest

# def reverse_integer(x: int) -> int:
#     result = 0
#     y = abs(x)
#     while y:
#         num = y % 10
#         y //= 10
#         result = (result * 10) + num
#
#     if x < 0:
#         return result * -1
#
#     return result


def reverse_integer(x: int) -> int:
    result = 0
    while x:
        num = int(math.fmod(x, 10))
        x = int(x / 10)
        result = (result * 10) + num

    return result


class Test(unittest.TestCase):
    def test1(self):
        x = 123
        got = reverse_integer(x)
        expected = 321
        self.assertEqual(expected, got)

    def test2(self):
        x = -123
        got = reverse_integer(x)
        expected = -321
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
