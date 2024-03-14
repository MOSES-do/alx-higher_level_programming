#!/usr/bin/python3
"""module to test string methods."""

import unittest

class TestStringMethods(unittest.TestCase):
    """simple unittests for strings methods."""

    def test_upper(self):
        """checks for an expected result."""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """verifies a specified condition."""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """verify that a specific exception gets raised."""
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == "__main__":
    unittest.main()
