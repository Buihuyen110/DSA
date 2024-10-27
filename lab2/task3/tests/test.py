import unittest

from lab2.task3.src.task3 import count_inversion

class TestCountInversion(unittest.TestCase):
    def test_no_inversions(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(count_inversion(arr), 0)

    def test_some_inversions(self):
        arr = [2, 3, 8, 6, 1]
        self.assertEqual(count_inversion(arr), 5)

    def test_all_inversions(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(count_inversion(arr), 10)

    def test_single_element(self):
        arr = [1]
        self.assertEqual(count_inversion(arr), 0)

    def test_empty_array(self):
        arr = []
        self.assertEqual(count_inversion(arr), 0)

    def test_random(self):
        arr = [1, 3, 5, 2, 4, 6]
        self.assertEqual(count_inversion(arr), 3)

if __name__ == '__main__':
    unittest.main()