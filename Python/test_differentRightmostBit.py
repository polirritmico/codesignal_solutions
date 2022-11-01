#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from differentRightmostBit import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        n = 11
        m = 13
        expected = 2
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        n = 7
        m = 23
        expected = 16
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        n = 1
        m = 0
        expected = 1
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        n = 64
        m = 65
        expected = 1
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        n = 1073741823
        m = 1071513599
        expected = 131072
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        n = 42
        m = 22
        expected = 4
        output = solution(n, m)
        self.assertEqual(output, expected)


