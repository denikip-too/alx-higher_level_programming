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

    def test_to_json_string(self):
        dictionary = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dictionary = Base.to_json_string([dictionary])
        a1 = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(json_dictionary, a1)

    def test_save_to_file(self):
        dict1 = {"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}
        dict2 = {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}
        a1 = '[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]'
        self.assertEqual(save_to_file[dict1, dict2], a1)

if __name__ == '__main__':
    unittest.main()
