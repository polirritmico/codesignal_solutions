#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from chessBoardCellColor import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        cell1 = "A1"
        cell2 = "C3"
        expected = True
        output = solution(cell1, cell2)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        cell1 = "B3"
        cell2 = "H8"
        expected = False
        output = solution(cell1, cell2)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        cell1 = "D2"
        cell2 = "D2"
        expected = True
        output = solution(cell1, cell2)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        cell1 = "A1"
        cell2 = "A2"
        expected = False
        output = solution(cell1, cell2)
        self.assertEqual(output, expected)

