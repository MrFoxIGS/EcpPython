import unittest

from scrabble import scrabble



class TestCase(unittest.TestCase):
    def test_two(self):
        self.assertEqual(scrabble('qi'), 11, msg="test 2 letter word qi")

    def test_three(self):
        self.assertEqual(scrabble('zax'), 18, msg="test 3 letter word zax")

    def test_capital(self):
        self.assertEqual(scrabble('ZAX'), 18, msg="test 3 letter word ZAX")

    def test_repeat(self):
        self.assertEqual(scrabble('zoom'), 15, msg="test word with repeated letters word zoom")

    def test_long1(self):
        self.assertEqual(scrabble('maximize'), 27, msg="test 8 letter word maximize")

    def test_long2(self):
        self.assertEqual(scrabble('quixotry'), 26, msg="test 8 letter word quixotry")

    def test_aaaaa(self):
        self.assertEqual(scrabble('aaaaa'), 5, msg="test repeated letters aaaaa")

    def test_nonAlpha(self):
        self.assertEqual(scrabble('Hello, World!'), 17, msg="test string with spaces and !, Hello, World!")

    def test_empty(self):
        self.assertEqual(scrabble(''), 0, msg="test empty string")


    def test_alphabet(self):
        self.assertEqual(scrabble('abcdefghijklmnopqrstuvwxyz'), 84, msg='test entire alphabet')
