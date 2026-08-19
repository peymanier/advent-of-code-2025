import unittest


def determine_majority(nums: list[int]) -> str:
    odd_count = 0
    for n in nums:
        odd_count += n % 2

    majority_needed = len(nums) // 2 + 1
    even_count = len(nums) - odd_count
    if odd_count == even_count:
        return "tie"

    if odd_count >= majority_needed:
        return "odd"
    else:
        return "even"


class TestMajority(unittest.TestCase):
    def test_majority_even(self):
        self.assertEqual(determine_majority([2, 4, 6, 1]), "even")

    def test_majority_odd(self):
        self.assertEqual(determine_majority([1, 3, 5, 2]), "odd")

    def test_all_even(self):
        self.assertEqual(determine_majority([0, 2, 4, 8]), "even")

    def test_all_odd(self):
        self.assertEqual(determine_majority([1, 3, 5, 7]), "odd")

    def test_tie(self):
        self.assertEqual(determine_majority([1, 2, 3, 4]), "tie")

    def test_empty_is_tie(self):
        self.assertEqual(determine_majority([]), "tie")

    def test_single_even(self):
        self.assertEqual(determine_majority([0]), "even")

    def test_single_odd(self):
        self.assertEqual(determine_majority([7]), "odd")

    def test_negatives(self):
        self.assertEqual(determine_majority([-2, -4, -1]), "even")
        self.assertEqual(determine_majority([-1, -3, -2]), "odd")

    def test_zero_counts_as_even(self):
        self.assertEqual(determine_majority([0, 1]), "tie")
        self.assertEqual(determine_majority([0, 2, 1]), "even")


if __name__ == "__main__":
    unittest.main()
