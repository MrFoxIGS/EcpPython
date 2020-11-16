import unittest

from hello_function import hello


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(hello(), "Hello, World!")
