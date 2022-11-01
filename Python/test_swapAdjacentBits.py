#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from swapAdjacentBits import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 13
        expected = 14
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = 74
        expected = 133
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = 1073741823
        expected = 1073741823
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = 0
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = 1
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = 83748
        expected = 166680
        output = solution(case)
        self.assertEqual(output, expected)


