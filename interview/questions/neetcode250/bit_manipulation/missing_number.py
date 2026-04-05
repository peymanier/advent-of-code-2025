import unittest

# def missing_number(nums: list[int]) -> int:
#     result = 0
#     for i in range(len(nums) + 1):
#         result ^= i
#         result ^= nums[i] if i < len(nums) else 0
#
#     return result


def missing_number(nums: list[int]) -> int:
    result = 0
    for i in range(len(nums) + 1):
        result += i
        result -= nums[i] if i < len(nums) else 0

    return result


class Test(unittest.TestCase):
    def test1(self):
        nums = [3, 0, 1]
        got = missing_number(nums)
        expected = 2
        self.assertEqual(expected, got)

    def test2(self):
        nums = [0, 1]
        got = missing_number(nums)
        expected = 2
        self.assertEqual(expected, got)

    def test3(self):
        nums = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]
        got = missing_number(nums)
        expected = 5
        self.assertEqual(expected, got)

    def test4(self):
        nums = [1, 2]
        got = missing_number(nums)
        expected = 0
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
