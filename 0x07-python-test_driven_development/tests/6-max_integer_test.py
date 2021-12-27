#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -8, -4, -12]), -1)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_max_of_less_positive_int(self):
        self.assertEqual(max_integer([1, 8, 5]), 8)

    def test_max_of_less_negative_int(self):
        self.assertEqual(max_integer([-3, -4, -14]), -3)

    def test_one_integer(self):
        self.assertEqual(max_integer([3]), 3)

if __name__ == '__main__':
    unittest.main()
