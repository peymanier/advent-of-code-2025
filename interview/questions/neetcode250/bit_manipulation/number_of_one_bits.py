import unittest

# def number_of_one_bits(n: int) -> int:
#     count = 0
#     while n > 0:
#         count += n % 2
#         n >>= 1
#
#     return count


def number_of_one_bits(n: int) -> int:
    count = 0
    while n > 0:
        n &= n - 1
        count += 1

    return count


class Test(unittest.TestCase):
    def test1(self):
        n = 11
        expected = 3
        got = number_of_one_bits(n)
        self.assertEqual(expected, got)

        n = 55
        expected = 5
        got = number_of_one_bits(n)
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
