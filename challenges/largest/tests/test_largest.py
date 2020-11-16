import unittest

from largest import list_largest




class LargestTest(unittest.TestCase):
    def test_single(self):
        self.assertEqual(list_largest([1]), 1)

    def test_same(self):
        self.assertEqual(list_largest([2, 2, 2, 2]), 2)

    def test_list_end(self):
        self.assertEqual(list_largest([1, 2, 3, 4, 5]), 5)

    def test_list_start(self):
        self.assertEqual(list_largest([5, 4, 3, 2, 1]), 5)

    def test_list_middle(self):
        self.assertEqual(list_largest([1, 2, 50, 3, 4]), 50)

    def test_list_neg(self):
        self.assertEqual(list_largest([-10, -5, -7]), -5)
