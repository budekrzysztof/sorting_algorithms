import unittest

from algorithms.MergeSort import MergeSort
from algorithms.BubbleSort import BubbleSort
from utility.Utils import Utils


class test_algorithms(unittest.TestCase):
    def test_bubble_asc(self):
        numbers = Utils().generate_random_numbers(0, 1000, 1000)
        sorted_numbers = numbers.copy()
        sorted_numbers.sort()
        self.assertListEqual(BubbleSort().sort_asc(numbers), sorted_numbers)

    def test_bubble_asc_empty(self):
        numbers = []
        self.assertListEqual(BubbleSort().sort_asc(numbers), [])

    def test_bubble_desc(self):
        numbers = Utils().generate_random_numbers(0, 1000, 1000)
        sorted_numbers = numbers.copy()
        sorted_numbers.sort()
        sorted_numbers.reverse()
        self.assertListEqual(BubbleSort().sort_desc(numbers), sorted_numbers)

    def test_bubble_desc_empty(self):
        numbers = []
        self.assertListEqual(BubbleSort().sort_desc(numbers), [])

    def test_merge_asc(self):
        numbers = Utils().generate_random_numbers(0, 1000, 1000)
        sorted_numbers = numbers.copy()
        sorted_numbers.sort()
        self.assertListEqual(MergeSort().sort_asc(numbers), sorted_numbers)

    def test_merge_asc_empty(self):
        numbers = []
        self.assertListEqual(MergeSort().sort_asc(numbers), [])

    def test_merge_desc(self):
        numbers = Utils().generate_random_numbers(0, 1000, 1000)
        sorted_numbers = numbers.copy()
        sorted_numbers.sort()
        sorted_numbers.reverse()
        self.assertListEqual(MergeSort().sort_desc(numbers), sorted_numbers)

    def test_merge_desc_empty(self):
        numbers = []
        self.assertListEqual(MergeSort().sort_desc(numbers), [])

if __name__ == '__main__':
    unittest.main()
