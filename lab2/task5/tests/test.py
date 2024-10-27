import unittest

from lab2.task5.src.task5 import find_majority_num

class TestMajorityNum(unittest.TestCase):

    def test_majority_exists(self):
        arr = [1, 2, 3, 2, 2]
        self.assertEqual(find_majority_num(arr), 1)  # Majority element is present

    def test_no_majority(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(find_majority_num(arr), 0)  # No majority element

    def test_all_elements_same(self):
        arr = [5, 5, 5, 5]
        self.assertEqual(find_majority_num(arr), 1)  # All are the same (majority)

    def test_large_input_with_majority(self):
        arr = [1]*100000 + [2]*50000 + [3]*20000
        self.assertEqual(find_majority_num(arr), 1)  # Majority is present

    def test_edge_case_single_element(self):
        arr = [7]
        self.assertEqual(find_majority_num(arr), 1)  # Single element is a majority

if __name__ == '__main__':
    unittest.main()