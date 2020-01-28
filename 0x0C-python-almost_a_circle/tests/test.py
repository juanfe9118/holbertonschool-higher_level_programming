#!/usr/bin/python3
"""Test Module for testing all the classes in the project"""


import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import models.rectangle
import models.square
import models.base

class TestCases(unittest.TestCase):
    """Class for all the tests"""

    def Tests(self):
        """All the tests"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        a = Base(89)
        self.assertEqual(a.id, 89)

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

        a = Square(2)
        self.assertEqual(a.size, 2)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 5)
        b = Square(3, 4, 5)
        self.assertEqual(b.size, 1)
        self.assertEqual(b.x, 4)
        self.assertEqual(b.y, 5)
        self.assertEqual(b.id, 6)
        c = Square(6, 5, 4, 12)
        self.assertEqual(c.size, 6)
        self.assertEqual(c.x, 5)
        self.assertEqual(c.y, 4)
        self.assertEqual(c.id, 12)

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

        a = Rectangle(4, 6)
        b = a.area()
        self.assertEqual(b, 24)
        a = Rectangle(4, 4, 3, 3)
        s = "\n\n\n   ####\n   ####\n   ####\n   ####\n"
        self.assertEqual(a.display(), s)
        a = Rectangle(1, 2, 3, 4, 5)
        s = "[Rectangle] (5) 3/4 - 1/2"
        self.assertEqual(str(a), s)

        a = Square(6, 8)
        self.assertEqual(a.area(), 36)
        a = Square(3, 3, 2)
        s = "\n\n   ###\n   ###\n   ###\n"
        self.assertEqual(a.display(), s)
        a = Square(5, 4, 3, 2)
        s = "[Square] (2) 4/3 - 5"
        self.assertEqual(str(a), s)

if __name__ == '__main__':
    unittest.main()
