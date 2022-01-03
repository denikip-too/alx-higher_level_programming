#!/usr/bin/python3
"""test square"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """tests for class Square"""

    def test_attributes(self):
        """test public getter and setter for size"""
        s1 = Square(5)
        s2 = Square(10)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s2.size, 10)

        with self.assertRaises(TypeError):
            s3 = Square("9")

        with self.assertRaises(ValueError):
            s4 = Square(-5)

    def test_update(self):
        """test update()"""
        s1 = Square(5)
        s1 = Square(1, 2, 3, 4)
        s1 = Square(size=7, id=89, y=1)
        self.assertEqual(s1.update(), [Square] (1) 0/0 - 5)
        self.assertEqual(s2.update(), [Square] (1) 3/4 - 2)
        self.assertEqual(s3.update(), [Square] (89) 12/1 - 7)

    def test_to_dictionary(self):
        """test dictionary representation of a Square"""
        s1 = Square(10, 2, 1)
        self.assertDictEqual(s1.to_dictionary(), 
                {'id': 1, 'x': 2, 'size': 10, 'y': 1})

if __name__ == '__main__':
    unittest.main()
