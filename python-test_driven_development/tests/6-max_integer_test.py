#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """should be executed by using this command:
    python3 -m unittest tests.6-max_integer_test
    """

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_element(self):
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-5, 0, 10, -3, 7])
        self.assertEqual(result, 10)

    def test_duplicate_numbers(self):
        result = max_integer([5, 5, 5, 5, 5])
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
