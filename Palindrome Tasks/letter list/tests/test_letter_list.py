import unittest

from LetterList import letter_list


class TestCase(unittest.TestCase):
    def test_capital(self):
        self.assertEqual(letter_list('Abba'),['a', 'b', 'b', 'a'] , msg="tests string with capitals")

    def test_capital(self):
        self.assertEqual(letter_list('Abba'),['a', 'b', 'b', 'a'] , msg="tests string with capitals")


    def test_redrum(self):
        self.assertEqual(letter_list('Red rum, sir, is murder'),['r', 'e', 'd', 'r', 'u', 'm', 's', 'i', 'r', 'i', 's', 'm', 'u', 'r', 'd', 'e', 'r'] , msg="tests string with capitals, non alpha and spaces")
