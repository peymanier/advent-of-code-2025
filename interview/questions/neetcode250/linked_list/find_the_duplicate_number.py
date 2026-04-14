import unittest


def find_duplicate(nums: list[int]) -> int:
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


class Test(unittest.TestCase):
    def test1(self):
        nums = [1, 3, 4, 2, 2]
        got = find_duplicate(nums)
        expected = 2
        self.assertEqual(expected, got)

    def test2(self):
        nums = [3, 1, 3, 4, 2]
        got = find_duplicate(nums)
        expected = 3
        self.assertEqual(expected, got)

    def test3(self):
        nums = [3, 3, 3, 3, 3]
        got = find_duplicate(nums)
        expected = 3
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
