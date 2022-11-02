#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from countSumOfTwoRepresentations2 import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        n = 6
        l = 2
        r = 4
        expected = 2
        output = solution(n, l, r)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        n = 6
        l = 3
        r = 3
        expected = 1
        output = solution(n, l, r)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        n = 10
        l = 9
        r = 11
        expected = 0
        output = solution(n, l, r)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        n = 24
        l = 8
        r = 16
        expected = 5
        output = solution(n, l, r)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        n = 24
        l = 12
        r = 12
        expected = 1
        output = solution(n, l, r)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        n = 93
        l = 24
        r = 58
        expected = 12
        output = solution(n, l, r)
        self.assertEqual(output, expected)


