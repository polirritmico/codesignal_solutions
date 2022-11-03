#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from appleBoxes import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 5
        expected = -15
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = 15
        expected = -120
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = 36
        expected = 666
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = 1
        expected = -1
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = 14
        expected = 105
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = 12
        expected = 78
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        case = 9
        expected = -45
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        case = 40
        expected = 820
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case9(self):
        case = 37
        expected = -703
        output = solution(case)
        self.assertEqual(output, expected)


