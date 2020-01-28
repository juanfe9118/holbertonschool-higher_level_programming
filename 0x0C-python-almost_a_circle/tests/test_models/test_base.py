#!/usr/bin/python3
"""Test Module for testing the Base class"""


import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import models.rectangle
import models.square
import models.base


class TestBase(unittest.TestCase):
    """Class for the tests"""

    def test_base(self):
        """The tests"""
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        a = Base(89)
        self.assertEqual(a.id, 89)
