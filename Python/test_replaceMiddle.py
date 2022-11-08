#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from replaceMiddle import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        case = [7, 2, 2, 5, 10, 7]
        expected = [7, 2, 7, 10, 7]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        case = [-5, -5, 10]
        expected = [-5, -5, 10]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        case = [45, 23, 12, 33, 12, 453, -234, -45]
        expected = [45, 23, 12, 45, 453, -234, -45]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        case = [2, 8]
        expected = [10]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        case = [-12, 34, 40, -5, -12, 4, 0, 0, -12]
        expected = [-12, 34, 40, -5, -12, 4, 0, 0, -12]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        case = [9, 0, 15, 9]
        expected = [9, 15, 9]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        case = [-6, 6, -6]
        expected = [-6, 6, -6]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        case = [26, 26, -17]
        expected = [26, 26, -17]
        output = solution(case)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case9(self):
        case = [-7, 5, 5, 10]
        expected = [-7, 10, 10]
        output = solution(case)
        self.assertEqual(output, expected)


