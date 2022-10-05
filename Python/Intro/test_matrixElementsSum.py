#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from matrixElementsSum import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_example(self):
        arguments = [[0, 1, 1, 2],
                     [0, 5, 0, 0],
                     [2, 0, 3, 3]]
        expected = 9
        output = solution(input)
        self.assertEqual(output, expected)

