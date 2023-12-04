#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from increaseNumberRoundness import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = 902200100
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = 11000
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = 99080
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = 1022220
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = 106611
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = 234230
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        case = 888
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        case = 100
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case9(self):
        case = 1000000000
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case10(self):
        case = 103456789
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


