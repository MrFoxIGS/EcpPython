import unittest

from palindrome import palindrome


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_single(self):
        self.assertEqual(palindrome('a'), True, msg="Test single character")

    def test_multiple(self):
        self.assertEqual(palindrome('aaaaa'), True, msg="Test the same character repeated")

    def test_even(self):
        self.assertEqual(palindrome('abba'), True, msg="Test even length palindrome")

    def test_odd(self):
        self.assertEqual(palindrome('tacocat'), True, msg="Test odd length palindrome")

    def test_not(self):
        self.assertEqual(palindrome('abbaa'), False, msg="Test not a palindrome")
