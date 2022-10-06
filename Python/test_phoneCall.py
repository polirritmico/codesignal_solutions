#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from phoneCall import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        min1 = 3
        min2_10 = 1
        min11 = 2
        s = 20
        expected = 14
        output = solution(min1, min2_10, min11, s)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case2(self):
        min1 = 2
        min2_10 = 2
        min11 = 1
        s = 2
        expected = 1
        output = solution(min1, min2_10, min11, s)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case3(self):
        min1 = 10
        min2_10 = 1
        min11 = 2
        s = 22
        expected = 11
        output = solution(min1, min2_10, min11, s)
        self.assertEqual(output, expected)

    def test_case4(self):
        min1 = 2
        min2_10 = 2
        min11 = 1
        s = 24
        expected = 14
        output = solution(min1, min2_10, min11, s)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case5(self):
        min1 = 1
        min2_10 = 2
        min11 = 1
        s = 6
        expected = 3
        output = solution(min1, min2_10, min11, s)
        self.assertEqual(output, expected)

    #@unittest.skip
    def test_case6(self):
        min1 = 10
        min2_10 = 10
        min11 = 10
        s = 8
        expected = 0
        output = solution(min1, min2_10, min11, s)
        self.assertEqual(output, expected)


