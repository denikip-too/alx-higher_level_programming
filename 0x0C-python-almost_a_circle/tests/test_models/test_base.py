#!/usr/bin/python3
"""unittest for Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """tests for class Base"""

    def test_id(self):
        """test for id attribute"""
        b1 = Base()
        b2 = Base()
        b3 = Base(40)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 40)
        self.assertEqual(b4.id, 3)

if __name__ == '__main__':
    unittest.main()
