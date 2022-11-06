#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from countBlackCells import *

class TestBase(unittest.TestCase):

    #@unittest.skip
    def test_case1(self):
        n = 3
        m = 4
        expected = 6
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case2(self):
        n = 3
        m = 3
        expected = 7
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case3(self):
        n = 2
        m = 5
        expected = 6
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case4(self):
        n = 1
        m = 1
        expected = 1
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case5(self):
        n = 1
        m = 2
        expected = 2
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case6(self):
        n = 1
        m = 3
        expected = 3
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case7(self):
        n = 1
        m = 239
        expected = 239
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case8(self):
        n = 33
        m = 44
        expected = 86
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case9(self):
        n = 16
        m = 8
        expected = 30
        output = solution(n, m)
        self.assertEqual(output, expected)


    #@unittest.skip
    def test_case10(self):
        n = 66666
        m = 88888
        expected = 177774
        output = solution(n, m)
        self.assertEqual(output, expected)


