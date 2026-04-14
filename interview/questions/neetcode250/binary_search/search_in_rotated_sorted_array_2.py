import unittest


def search(nums: list[int], target: int) -> bool:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True

        if nums[mid] > nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] < nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            left += 1

    return False


class Test(unittest.TestCase):
    def test1(self):
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 0
        got = search(nums, target)
        expected = True
        self.assertEqual(expected, got)

    def test2(self):
        nums = [2, 5, 6, 0, 0, 1, 2]
        target = 7
        got = search(nums, target)
        expected = False
        self.assertEqual(expected, got)

    def test3(self):
        nums = [4, 5, 6, 6, 7, 0, 1, 2, 4, 4]
        target = 2
        got = search(nums, target)
        expected = True
        self.assertEqual(expected, got)

    def test4(self):
        nums = [4, 5, 6, 6, 7, 0, 1, 2, 4, 4]
        target = 5
        got = search(nums, target)
        expected = True
        self.assertEqual(expected, got)

    def test5(self):
        nums = [4, 5, 6, 6, 7, 0, 1, 2, 4, 4]
        target = 3
        got = search(nums, target)
        expected = False
        self.assertEqual(expected, got)

    def test6(self):
        nums = [2, 2, 3, 1, 2, 2]
        target = 1
        got = search(nums, target)
        expected = True
        self.assertEqual(expected, got)

    def test7(self):
        nums = [1, 0, 1, 1, 1]
        target = 0
        got = search(nums, target)
        expected = True
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
