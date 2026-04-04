import unittest


def counting_bits_alt(num: int) -> list[int]:
    # def count(n: int):
    #     result = 0
    #     while n > 0:
    #         n &= n - 1
    #         result += 1
    #
    #     return result

    def count(n: int):
        result = 0
        while n > 0:
            result += n % 2
            n >>= 1

        return result

    # def count(n: int):
    #     result = 0
    #     while n > 0:
    #         result += n % 2
    #         n //= 2
    #
    #     return result

    result = []
    for i in range(0, num + 1):
        result.append(count(i))

    return result


# def counting_bits(num: int) -> list[int]:
#     if num < 1:
#         return [0]
#
#     def most_significant_bit(n: int) -> int:
#         count = 0
#         while n > 0:
#             n >>= 1
#             count += 1
#
#         return count
#
#     dp = [0 for _ in range(num + 1)]
#     dp[0] = 0
#     for i in range(1, num + 1):
#         k = most_significant_bit(i)
#         dp[i] = 1 + dp[i - 2 ** (k - 1)]
#
#     return dp


# def counting_bits(num: int) -> list[int]:
#     if num < 1:
#         return [0]
#
#     import math
#
#     def calc_offset(n: int) -> int:
#         return 2 ** int(math.log2(n))
#
#     dp = [0 for _ in range(num + 1)]
#     for i in range(1, num + 1):
#         offset = calc_offset(i)
#         dp[i] = 1 + dp[i - offset]
#
#     return dp


def counting_bits(num: int) -> list[int]:
    dp = [0 for _ in range(num + 1)]
    offset = 1
    for i in range(1, num + 1):
        if offset * 2 == i:
            offset = i

        dp[i] = 1 + dp[i - offset]

    return dp


class Test(unittest.TestCase):
    def test1(self):
        n = 0
        expected = [0]
        got = counting_bits(n)
        self.assertEqual(expected, got)

        n = 2
        expected = [0, 1, 1]
        got = counting_bits(n)
        self.assertEqual(expected, got)

        n = 8
        expected = [0, 1, 1, 2, 1, 2, 2, 3, 1]
        got = counting_bits(n)
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
