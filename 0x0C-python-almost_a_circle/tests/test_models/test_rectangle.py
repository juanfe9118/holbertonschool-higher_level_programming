#!/usr/bin/python3
"""Test Module for testing the Rectangle class"""


import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import models.rectangle
import models.square
import models.base

class Test_Rectangle(unittest.TestCase):
    """Class for all the tests"""

    def test_rectangle(self):
        """All the tests"""
        a = Rectangle(8, 5)
        self.assertEqual(a.width, 8)
        self.assertEqual(a.height, 5)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 3)
        b = Rectangle(5, 1, 9, 2)
        self.assertEqual(b.width, 5)
        self.assertEqual(b.height, 1)
        self.assertEqual(b.x, 9)
        self.assertEqual(b.y, 2)
        self.assertEqual(b.id, 4)
        c = Rectangle(9, 7, 6, 4, 34)
        self.assertEqual(c.width, 9)
        self.assertEqual(c.height, 7)
        self.assertEqual(c.x, 6)
        self.assertEqual(c.y, 4)
        self.assertEqual(c.id, 34)

        with self.assertRaises(TypeError, msg='width must be an integer'):
            a = Rectangle("python", 8)
        with self.assertRaises(ValueError, msg='width must be > 0'):
            f = Rectangle(-6, 4)
        with self.assertRaises(TypeError, msg='height must be an integer'):
            s = Rectangle(9, "hello")
        with self.assertRaises(ValueError, msg='height must be > 0'):
            g = Rectangle(4, -9)
        with self.assertRaises(TypeError, msg='x must be an integer'):
            e = Rectangle(5, 9, [3, 2])
        with self.assertRaises(ValueError, msg='x must be > 0'):
            t = Rectangle(1, 8, -7)
        with self.assertRaises(TypeError, msg='y must be an integer'):
            j = Rectangle(4, 2, 7, "world")
        with self.assertRaises(ValueError, msg='y must be > 0'):
            r = Rectangle(3, 1, 9, -9)

        a = Rectangle(1, 2, 3, 4, 5)
        s = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(str(a), s)
