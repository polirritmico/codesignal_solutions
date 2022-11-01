#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from secondRightmostZeroBit import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 37
        expected = 8
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = 1073741824
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = 83748
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = 4
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = 728782938
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)


