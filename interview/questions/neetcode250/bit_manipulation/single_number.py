import unittest


def single_number(nums: list[int]) -> int:
    result = 0
    for n in nums:
        result ^= n

    return result


class Test(unittest.TestCase):
    def test1(self):
        nums = [2, 2, 1]
        expected = 1
        got = single_number(nums)
        self.assertEqual(expected, got)

    def test2(self):
        nums = [4, 1, 2, 1, 2]
        expected = 4
        got = single_number(nums)
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
