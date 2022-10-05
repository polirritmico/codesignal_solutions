#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from adjacentElementsProduct import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_example(self):
        array = [1, 2, 3]
        expected = 6
        output = adjProduct(array)

        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        array = [-23, 4, -3, 8, -12]
        expected = -12
        output = adjProduct(array)

        self.assertEqual(output, expected)
