#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from absoluteValuesSumMinimization import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [2, 4, 7]
        expected = 4
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        case = [2, 3]
        expected = 2
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        case = [1, 1, 3, 4]
        expected = 1
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case4(self):
        case = [23]
        expected = 23
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        case = [-10, -10, -10, -10, -10, -9, -9, -9, -8, -8, -7, -6, -5, -4,
                -3, -2, -1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44,
                45, 46, 47, 48, 49, 50]
        expected = 15
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        case = [-4, -1]
        expected = -4
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case7(self):
        case = [0, 7, 9]
        expected = 7
        output = solution(case)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case8(self):
        case = [-1000000, -10000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100,
                1000, 10000, 100000, 1000000]
        expected = 0
        output = solution(case)
        self.assertEqual(output, expected)



