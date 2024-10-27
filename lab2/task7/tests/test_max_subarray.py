import unittest
from random import randint

from lab2.task7.src.task7 import find_max_subarray


class TestMaxSubarray(unittest.TestCase):

    def test_find_max_subarray_length_1000(self):
        arr = [randint(-10 ** 9, 10 ** 9) for _ in range(1000)]  # Sửa đổi ở đây
        start, end, max_sum = find_max_subarray(arr)
        self.assertIsInstance(max_sum, int)

    def test_find_max_subarray_length_10000(self):
       arr = [randint(-10 ** 9, 10 ** 9) for _ in range(10000)]
       start, end, max_sum = find_max_subarray(arr)
       self.assertIsInstance(max_sum, int)

    def test_find_max_subarray_length_100000(self):
       arr = [randint(-10 ** 9, 10 ** 9) for _ in range(100000)]
       start, end, max_sum = find_max_subarray(arr)
       self.assertIsInstance(max_sum, int)


if __name__ == '__main__':
   unittest.main()

