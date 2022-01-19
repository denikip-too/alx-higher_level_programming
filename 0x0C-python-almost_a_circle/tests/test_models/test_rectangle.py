#!/usr/bin/python3
"""unitest for class Rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tests for class Rectangle"""

    """def test_id(self):
        test for id attribute
        r1 = Rectangle(10, 2, 4, 5, 1)
        r2 = Rectangle(2, 10, 5, 7, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, Rectangle._Base__nb_objects)
        self.assertEqual(r2.id, Rectangle._Base__nb_objects)
        self.assertEqual(r3.id, Rectangle._Base__nb_objects)"""

    def test_attribute_validation(self):
        """attribute validation testing"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2")
            r2 = Rectangle(10, 2, {}, 3)
            r3 = Rectangle(10, 2, 3, {})

        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 0)
            r5 = Rectangle(-2, 10)
            r6 = Rectangle(10, 2, -5, 5)
            r7 = Rectangle(10, 2, 5, -6)

    def test_area(self):
        """tests area"""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    """def test_display(self):
        r1 = Rectangle(4, 6)
        d1 = '####\n####\n####\n####\n####\n####'
        r2 = Rectangle(2, 2)
        d2 = '####\n####'
        self.assertEqual(r1.display(), d1)
        self.assertSequenceEqual(r2.display(), d2)"""

    def test_str(self):
        """tests for attributes of Rectangle"""
        r1 = Rectangle(5, 5, 1, 0, 1)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 1/0 - 5/5')

    def test_to_dictionary(self):
        """test dictionary representation of a Rectangle"""
        r1 = Rectangle(10, 2, 1, 9, 1)
        self.assertDictEqual(r1.to_dictionary(), 
                {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})

if __name__ == '__main__':
    unittest.main()
