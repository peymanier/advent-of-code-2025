import unittest

matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5],
]

# def range_sum(up_left: tuple[int, int], down_right: tuple[int, int]) -> int:
#     result = 0
#     for r in range(up_left[0], down_right[0] + 1):
#         for c in range(up_left[1], down_right[1] + 1):
#             result += matrix[r][c]
#
#     return result


def matrix_prefix_sum() -> list[list[int]]:
    rows_len = len(matrix)
    cols_len = len(matrix[0])

    result = [[0 for _ in range(cols_len)] for _ in range(rows_len)]
    for r in range(rows_len):
        curr_sum = 0
        for c in range(cols_len):
            curr_sum += matrix[r][c]

            result[r][c] = curr_sum
            if r - 1 >= 0:
                result[r][c] += result[r - 1][c]

    return result


def range_sum(up_left: tuple[int, int], down_right: tuple[int, int]) -> int:
    prefix_sum = matrix_prefix_sum()
    r1, c1 = up_left
    r2, c2 = down_right

    bottom_right = prefix_sum[r2][c2]
    above = 0
    if c1 - 1 >= 0:
        above = prefix_sum[r2][c1 - 1]

    left = 0
    if r1 - 1 >= 0:
        left = prefix_sum[r1 - 1][c2]

    top_left = 0
    if r1 - 1 >= 0 and c1 - 1 >= 0:
        top_left = prefix_sum[r1 - 1][c1 - 1]

    return bottom_right - left - above + top_left


class Test(unittest.TestCase):
    def test1(self):
        x = (1, 1)
        y = (2, 2)
        got = range_sum(x, y)
        expected = 11
        self.assertEqual(expected, got)

    def test2(self):
        x = (1, 2)
        y = (2, 4)
        got = range_sum(x, y)
        expected = 12
        self.assertEqual(expected, got)

    def test3(self):
        x = (2, 1)
        y = (4, 3)
        got = range_sum(x, y)
        expected = 8
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
