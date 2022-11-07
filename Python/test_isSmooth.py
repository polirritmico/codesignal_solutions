#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from isSmooth import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [7, 2, 2, 5, 10, 7]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = [-5, -5, 10]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = [4, 2]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = [45, 23, 12, 33, 12, 453, -234, -45]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = [-12, 34, 40, -5, -12, 4, 0, 0, -12]
        expected = True
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = [9, 0, 15, 9]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        case = [-6, 6, -6]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        case = [26, 26, -17]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case9(self):
        case = [-7, 5, 5, 10]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case10(self):
        case = [3, 4, 5]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.ski
    def test_case11(self):
        case = [-5, 3, -1, 9]
        expected = False
        output = solution(case)
        self.assertEqual(output, expected)


