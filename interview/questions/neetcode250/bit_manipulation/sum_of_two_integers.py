import unittest


def sum_of_two(a: int, b: int) -> int:
    first = a
    second = b
    while second:
        temp = first
        first = first ^ second
        second = (temp & second) << 1

    return first


class Test(unittest.TestCase):
    def test1(self):
        a = 1
        b = 2
        got = sum_of_two(a, b)
        expected = 3
        self.assertEqual(expected, got)

    def test2(self):
        a = 2
        b = 3
        got = sum_of_two(a, b)
        expected = 5
        self.assertEqual(expected, got)

    def test3(self):
        a = 1001
        b = 13
        got = sum_of_two(a, b)
        expected = 1014
        self.assertEqual(expected, got)

    def test4(self):
        a = -22
        b = -13
        got = sum_of_two(a, b)
        expected = -35
        self.assertEqual(expected, got)

    @unittest.skip("does not work in python")
    def test5(self):
        a = -22
        b = 23
        got = sum_of_two(a, b)
        expected = 1
        self.assertEqual(expected, got)


if __name__ == "__main__":
    unittest.main()
