#!/usr/bin/python3
"""Test Module for testing the Square class"""


import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import models.rectangle
import models.square
import models.base


class TestSquare(unittest.TestCase):
    """Class for all the tests"""

    def test_square(self):
        """All the tests"""
        a = Square(2)
        self.assertEqual(a.size, 2)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 5)
        b = Square(3, 4, 5)
        self.assertEqual(b.size, 3)
        self.assertEqual(b.x, 4)
        self.assertEqual(b.y, 5)
        self.assertEqual(b.id, 6)
        c = Square(6, 5, 4, 12)
        self.assertEqual(c.size, 6)
        self.assertEqual(c.x, 5)
        self.assertEqual(c.y, 4)
        self.assertEqual(c.id, 12)

        with self.assertRaises(TypeError, msg='width must be an integer'):
            w = Square("hi", 6)
        with self.assertRaises(ValueError, msg='width must be > 0'):
            o = Square(-1, 4)
        with self.assertRaises(TypeError, msg='x must be an integer'):
            r = Square(3, "e")
        with self.assertRaises(ValueError, msg='x must be > 0'):
            l = Square(2, 4, -8)
        with self.assertRaises(TypeError, msg='y must be an integer'):
            d = Square(5, 8, set([1, 2, 3, 4]))
        with self.assertRaises(ValueError, msg='y must be > 0'):
            s = Square(6, 7, -4)

        a = Square(5, 4, 3, 2)
        s = "[Square] (2) 4/3 - 5"
        self.assertEqual(str(a), s)
