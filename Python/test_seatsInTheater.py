#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from seatsInTheater import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        nCols = 16
        nRows = 11
        col = 5
        row = 3
        expected = 96
        output = solution(nCols, nRows, col, row)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        nCols = 13
        nRows = 6
        col = 8
        row = 3
        expected = 18
        output = solution(nCols, nRows, col, row)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        nCols = 1000
        nRows = 1000
        col = 1000
        row = 1000
        expected = 0
        output = solution(nCols, nRows, col, row)
        self.assertEqual(output, expected)


