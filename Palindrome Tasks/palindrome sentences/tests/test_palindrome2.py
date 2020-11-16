import unittest

from palindrome2 import palindrome2


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_single(self):
        self.assertEqual(palindrome2('my gym'), True, msg="Test 2 word with space")

    def test_multiple(self):
        self.assertEqual(palindrome2('Step on no pets'), True, msg="Test 4 word with capital")

    def test_even(self):
        self.assertEqual(palindrome2('Eva, can I see bees in a cave?'), True, msg="Test long with capitals and punctuation")

    def test_not(self):
        self.assertEqual(palindrome2('The quick brown fox jumps over the lazy dog'), False, msg="Test not a palindrome")
