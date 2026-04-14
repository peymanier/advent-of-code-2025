import unittest


def find_minimum(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    result = float("inf")
    while left <= right:
        if nums[left] <= nums[right]:
            return min(result, nums[left])

        mid = (left + right) // 2
        result = min(result, nums[mid])

        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid - 1

    return result


class Test(unittest.TestCase):
    def test1(self):
        nums = [3, 4, 5, 1, 2]
        got = find_minimum(nums)
        expected = 1
        self.assertEqual(expected, got)

    def test2(self):
        nums = [0, 1, 2, 4, 5, 6, 7]
        got = find_minimum(nums)
        expected = 0
        self.assertEqual(expected, got)

    def test3(self):
        nums = [3, 5, 7, 11, 13, 17, 19, 2]
        got = find_minimum(nums)
        expected = 2
        self.assertEqual(expected, got)

    def test4(self):
        nums = [20, 2, 3, 5, 7, 11, 13, 17, 19]
        got = find_minimum(nums)
        expected = 2
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
