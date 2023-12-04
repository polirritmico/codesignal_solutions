#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from concatenateArrays import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        a = [2, 2, 1]
        b = [10, 11]
        expected = [2, 2, 1, 10, 11]
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        a = [1, 2]
        b = [3, 1, 2]
        expected = [1, 2, 3, 1, 2]
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        a = [1]
        b = []
        expected = [1]
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        a = [2, 10, 3, 9, 5, 11, 11]
        b = [4, 8, 1, 13, 3, 1, 14]
        expected = [2, 10, 3, 9, 5, 11, 11, 4, 8, 1, 13, 3, 1, 14]
        output = solution(a, b)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        a = [9, 6, 6, 9, 8, 14]
        b = [3, 2, 2, 5, 3, 11, 12, 9, 7, 7]
        expected = [9, 6, 6, 9, 8, 14, 3, 2, 2, 5, 3, 11, 12, 9, 7, 7]
        output = solution(a, b)
        self.assertEqual(output, expected)


