import unittest

from lab2.task4.src.task4 import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_element_found(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 3), 2)  # Index of element 3

    def test_element_not_found(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 6), -1)  # Element not in array

    def test_empty_array(self):
        arr = []
        self.assertEqual(binary_search(arr, 1), -1)  # Searching in an empty array

    def test_multiple_occurrences(self):
        arr = [1, 2, 3, 3, 4]
        self.assertEqual(binary_search(arr, 3), 2)  # Should return the first occurrence index

class TestCountIndices(unittest.TestCase):

    def test_all_elements_found(self):
        list1 = [1, 2, 3, 4]
        list2 = [2, 3]
        self.assertEqual(count_indices(list1, list2), [1, 2])

    def test_some_elements_not_found(self):
        list1 = [10, 20, 30]
        list2 = [5, 10]
        self.assertEqual(count_indices(list1, list2), [-1, 0])

    def test_empty_list(self):
        list1 = []
        list2 = [10]
        self.assertEqual(count_indices(list1, list2), [-1])

    def test_no_elements_in_second_list(self):
        list1 = [10, 20]
        list2 = []
        self.assertEqual(count_indices(list1, list2), [])

if __name__ == '__main__':
    unittest.main()